#!/usr/bin/env python3
from gpiozero import MCP3002, LED
import warnings
import threading
from time import sleep

# ignore warnings from gpiozero
warnings.simplefilter('ignore')

# continue condition
continue_sensing = True


def convert_temp(temp_gen):
    '''
    takes in a temperature sensor generator and returns a generator of the
    values converted to Fahrenheit.
    '''
    for value in temp_gen:
        celcius = (value * 3.3 - 0.5) * 100

        # yield the result in Fahrenheit
        yield (celcius * (9 / 5)) + 32


def monitor_temp(temp_sensor, temp_led):
    '''
    takes in a temperature sensor and led and toggles the led on if the
    temperature reaches a maximum of 78 degrees Fahrenheit.
    '''
    for temp in convert_temp(temp_sensor.values):
        print("The temperature is: {:.2f}F".format(temp))
        if temp > 78:
            temp_led.on()
        else:
            temp_led.off()

        # should the thread continue reading from the sensor
        if continue_sensing:
            sleep(1)
        else:
            break


def monitor_light(light_sensor, light_led):
    for level in light_sensor.values:
        level *= 100
        print("The light level is: {:.2f}".format(level))
        if level < 40:
            light_led.on()
        else:
            light_led.off()

        # should the thread continue reading form the sensor
        if continue_sensing:
            sleep(1)
        else:
            break


if __name__ == "__main__":
    # create the leds
    temp_led = LED("GPIO27")
    light_led = LED("GPIO22")

    # create the sensor channels on the MCP3002
    temp_sensor = MCP3002(channel=0)
    light_sensor = MCP3002(channel=1)

    # create a separate thread for each sensor
    temp_thread = threading.Thread(target=monitor_temp, args=(temp_sensor,
                                                              temp_led))
    light_thread = threading.Thread(target=monitor_light, args=(light_sensor,
                                                                light_led))
    print("Hit 'Q' to Quit")

    # start checking each sensor
    temp_thread.start()
    light_thread.start()

    # allow the user to exit the program by pressing 'q'
    while continue_sensing:
        c = input()
        if c.upper() == 'Q':
            continue_sensing = False

    # wait for the threads to exit
    temp_thread.join()
    light_thread.join()

    # ensure leds and sensors are closed out properly
    light_led.close()
    light_sensor.close()
    temp_sensor.close()
    temp_led.close()
