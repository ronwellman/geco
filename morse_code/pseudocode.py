#!/usr/bin/env python3

from morse_code import encode
import RPi.GPIO as GPIO
import time

buzzer = 17
unit = .1
'''
There are rules to help people distinguish dots from dashes in Morse code.
The length of a dot is 1 time unit.
A dash is 3 time units.
The space between symbols (dots and dashes) of the same letter is 1 time unit.
The space between letters is 3 time units.
The space between words is 7 time units.
http://www.codebug.org.uk/learn/step/541/morse-code-timing-rules/
'''


def setup():
    '''
    setup() -> NoneType

    Setup RPi GPIO base parameters.
    '''
    # BCM so GPIO pin numbers match

    # buzzer is an output device

    # PNP transistor - High stops flow, Low allows flow


def teardown():
    '''
    teardown() -> NoneType

    Restore RPi GPIO parameters.
    '''
    # reset RPi GPIO before exiting


def play_dot():
    '''
    play_dot() -> NoneType

    Play a morse code dot (short).
    '''
    # The length of a dot is 1 time unit.

    # The space between symbols of the same letter is 1 time unit.


def play_dash():
    '''
    play_dash() -> NoneType

    Play a morse code dash (long).
    '''
    # A dash is 3 time units.

    # The space between symbols of the same letter is 1 time unit.


def main():
    '''
    main -> int

    Prompt user for text, translate that text into morse code, and then sent
    the resulting dots and dashes to the buzzer.
    '''
    try:
        # infinite loop
        while True:

            # prompt the user for input

            # translate the input into morse code

            # play the dots and dashes on the buzzer

    # catch ctrl-c

    print()
    return 0


if __name__ == "__main__":
    # initialize the RPi GPIO interface
    
    # run the main program

    # restore the RPi GPIO interface
