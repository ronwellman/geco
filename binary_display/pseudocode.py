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
        #
        # INSERT CODE HERE
        #


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
    
    
    # iterates from Least Significant Bit (LSB) to Most Significant Bit (MSB)
    # by checking if the number is odd, and then shifting one bit to the right
    # until number is zero
    while number:

        # set light HIGH if odd and LOW if even
        #
        # INSERT CODE HERE
        #

        # update index
        #
        # INSERT CODE HERE
        #

        # shift bits to the right by one
        #
        # INSERT CODE HERE
        #


def clear_display():
    '''
    clear_display() -> None

    Sets all of the LEDs to low
    '''
    # loop through the LEDs and set them to low



def main():
    '''
    main -> int

    Add four binary bits together and display results to LEDs.
    '''
    try:
        # infinite loop
        while True:

            # get the number from the user
            #
            # INSERT CODE HERE
            #

            try:

                # attempt to convert the number
                #
                # INSERT CODE HERE
                #

                # test the range of the number
                #
                # INSERT CODE HERE
                #

            except ValueError:
                print("Invalid number: {}".format(number))
                continue

            # output the number to the LEDs
            #
            # INSERT CODE HERE
            #

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
