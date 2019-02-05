#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

# The GPIO numbers are enterd backwards from actual placement on the board
# leds[0] cooresponsds to Least Significant Bit (LSB - rightmost LED)
# buttons[0] corresponds to LSB
leds = [19, 13, 22, 27, 17]
buttons = [25, 24, 23, 18, 21]

# bits are backwards and correspond to [2^0, 2^1, 2^2, 2^3]
bits = [0, 0, 0, 0]

# results is the sum
result = 0

# Mode 0 - First Entry, Mode 1 - Second Entry, Mode 3 - Display Sum
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
        # Detects the release of a button and ignores bouncing for 300 ms
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
    # marked global to ensure it references the global mode and result since
    # assignments in this function that will cause python to refer to them
    # as local variables.
    global mode
    global result

    # GPIO21 is the add button
    if button != 21:

        # find the index value (buttons list) of the button that was pressed
        # and used that index to update the leds list and bits list
        index = buttons.index(button)
        if bits[index] == 0:
            bits[index] = 1
            GPIO.output(leds[index], GPIO.HIGH)
        else:
            bits[index] = 0
            GPIO.output(leds[index], GPIO.LOW)
    else:

        # add button was pressed, check mode and update accordingly
        # Mode 0 - First Entry, Mode 1 - Second Entry, Mode 3 - Display Sum
        if mode == 0:
            add_number()
            mode += 1
            clear_leds()
        elif mode == 1:
            add_number()
            mode += 1
            display_sum()
        else:
            mode = 0
            result = 0
            clear_leds()


def add_number():
    '''
    add_number() -> None

    Sum the binary bits and store the result.
    '''
    # marked global to ensure it references the global result since
    # assignments in this function will cause python to refer to it as a local
    # variable
    global result

    # since bits are already in reverse order, iterate through in order
    for index, bit in enumerate(bits):
        if bit:
            result += 2**index

    print(result, end='')

    if mode == 0:
        print(' + ', end='')
    else:
        print('= ', end='')


def clear_leds():
    '''
    clear_leds() -> None

    Turns each of the LEDs off.
    '''
    for led in leds:
        GPIO.output(led, GPIO.LOW)

    for index in range(len(bits)):
        bits[index] = 0


def display_sum():
    '''
    display_sum() -> None

    Display the sum in binary on the LEDs.
    '''
    # display result without destroying result
    temp = result
    index = 0

    # iterates from Least Significant Bit (LSB) to Most Significant Bit (MSB)
    # by checking if the number is odd, and then shifting one bit to the right
    # until temp is zero
    while temp:

        # check if odd
        if temp % 2 == 1:
            GPIO.output(leds[index], GPIO.HIGH)
        else:
            GPIO.output(leds[index], GPIO.LOW)
        index += 1

        # shift bits to the right by one
        temp = temp >> 1


def main():
    '''
    main -> int

    Add four binary bits together and display results to LEDs.
    '''
    try:
        # infinite loop
        while True:
            # main loop only sleeps as button pushes are automatically caught
            # via GPIO.add_event_detect
            time.sleep(1)

    # catch ctrl-c
    except KeyboardInterrupt:
        pass

    print()
    return 0


if __name__ == "__main__":
    # initialize the RPi GPIO interface
    setup()

    # run the main loop
    main()

    # restore the RPi GPIO interface
    teardown()
