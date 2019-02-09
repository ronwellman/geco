#!/usr/bin/env python3

import RPi.GPIO as GPIO

# The GPIO numbers are entered backwards from actual placement on the board
# leds[0] corresponds to Least Significant Bit (LSB - rightmost LED)
leds = [19, 13, 22, 27, 17]


def setup():
    '''
    setup() -> NoneType

    Setup RPi GPIO base parameters.
    '''
    # BCM so GPIO pin numbers match
    GPIO.setmode(GPIO.BCM)

    for led in leds:
        # set the LEDs as input devices and set low
        GPIO.setup(led, GPIO.OUT)
        GPIO.output(led, GPIO.LOW)


def teardown():
    '''
    teardown() -> NoneType

    Restore RPi GPIO parameters.
    '''
    # reset RPi GPIO before exiting
    GPIO.cleanup()


def display_binary(number):
    '''
    display_binary() -> None

    Display the binary number on the LEDs.
    '''
    index = 0

    # clear all lights before displaying the new ones
    clear_display()

    # iterates from Least Significant Bit (LSB) to Most Significant Bit (MSB)
    # by checking if the number is odd, and then shifting one bit to the right
    # until number is zero
    while number:

        # check if odd
        if number % 2 == 1:
            GPIO.output(leds[index], GPIO.HIGH)
        index += 1

        # shift bits to the right by one
        number = number >> 1


def clear_display():
    '''
    clear_display() -> None

    Sets all of the LEDs to low
    '''
    # loop through the LEDs and set them to low
    for led in leds:
        GPIO.output(led, GPIO.LOW)


def main():
    '''
    main -> int

    Add four binary bits together and display results to LEDs.
    '''
    try:
        # infinite loop
        while True:

            # get the number from the user
            number = input("Enter a number to convert and display (0 - 31): ")
            try:

                # attempt to convert the number
                number = int(number)

                # test the range of the number
                if not(0 <= number <= 31):
                    raise ValueError

            except ValueError:
                print("Invalid number: {}".format(number))
                continue

            # output the number to the LEDs
            display_binary(number)

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
