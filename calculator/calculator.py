#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

leds = [19, 13, 22, 27, 17]
buttons = [25, 24, 23, 18, 21]
addends = [0, 0, 0, 0]
result = 0
mode = 0


def setup():
    '''
    setup() -> NoneType

    Setup RPi GPIO base parameters.
    '''
    # BCM so GPIO pin numbers match
    GPIO.setmode(GPIO.BCM)

    for led in leds:
        GPIO.setup(led, GPIO.OUT)
        GPIO.output(led, GPIO.LOW)

    for button in buttons:
        GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)
        GPIO.add_event_detect(button, GPIO.RISING, button_push, 300)


def teardown():
    '''
    teardown() -> NoneType

    Restore RPi GPIO parameters.
    '''
    # reset RPi GPIO before exiting
    GPIO.cleanup()


def button_push(button):
    '''
    button_push(int) -> None

    Updates the LEDs and mode according the the button that was pushed.
    '''
    global mode
    global result
    if button != 21:
        index = buttons.index(button)
        if addends[index] == 0:
            addends[index] = 1
            GPIO.output(leds[index], GPIO.HIGH)
        else:
            addends[index] = 0
            GPIO.output(leds[index], GPIO.LOW)
    else:
        if mode == 0:
            mode += 1
            add_number()
            clear_leds()
        elif mode == 1:
            mode += 1
            add_number()
            display_sum()
        else:
            mode = 0
            result = 0
            clear_leds()


def add_number():
    '''
    add_number() -> None

    Sum the binary digits and store the result.
    '''
    global result
    position = 0
    for digit in addends:
        if digit:
            result += 2**position
        position += 1
    print(result)


def clear_leds():
    '''
    clear_leds() -> None

    Turns each of the LEDs off.
    '''
    for led in leds:
        GPIO.output(led, GPIO.LOW)

    for index in range(len(addends)):
        addends[index] = 0


def display_sum():
    '''
    display_sum() -> None

    Display the sum in binary on the LEDs.
    '''
    temp = result
    index = 0
    while temp:
        if temp % 2 == 1:
            GPIO.output(leds[index], GPIO.HIGH)
        else:
            GPIO.output(leds[index], GPIO.LOW)
        index += 1
        temp = temp >> 1


def main():
    '''
    main -> int

    Add four binary bits together and display results to LEDs.
    '''
    try:
        # infinite loop
        while True:
            time.sleep(1)

    # catch ctrl-c
    except KeyboardInterrupt:
        pass

    print()
    return 0


if __name__ == "__main__":
    # initialize the RPi GPIO interface
    setup()

    main()

    # restore the RPi GPIO interface
    teardown()
