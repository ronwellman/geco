#!/usr/bin/env python3

from morse_code import encode
import RPi.GPIO as GPIO
import time

buzzer = 17
unit = .1

# 8550 -> PNP
# 8050 -> NPN
# 2222 -> NPN
trans = 'PNP'


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
    GPIO.setmode(GPIO.BCM)

    # buzzer is an output device
    GPIO.setup(buzzer, GPIO.OUT)

    # PNP transistor - High stops flow, Low allows flow
    # NPN transistor - Low stops flow, High allows flow
    if trans == 'PNP':
        GPIO.output(buzzer, GPIO.HIGH)
    elif trans == 'NPN':
        GPIO.output(buzzer, GPIO.LOW)


def teardown():
    '''
    teardown() -> NoneType

    Restore RPi GPIO parameters.
    '''
    # reset RPi GPIO before exiting
    GPIO.cleanup()


def play_dot():
    '''
    play_dot() -> NoneType

    Play a morse code dot (short).
    '''
    # The length of a dot is 1 time unit.
    GPIO.output(buzzer, GPIO.LOW if trans == 'PNP' else GPIO.HIGH)
    time.sleep(1 * unit)

    # The space between symbols of the same letter is 1 time unit.
    GPIO.output(buzzer, GPIO.HIGH if trans == 'PNP' else GPIO.LOW)
    time.sleep(1 * unit)


def play_dash():
    '''
    play_dash() -> NoneType

    Play a morse code dash (long).
    '''
    # A dash is 3 time units.
    GPIO.output(buzzer, GPIO.LOW if trans == 'PNP' else GPIO.HIGH)
    time.sleep(3 * unit)

    # The space between symbols of the same letter is 1 time unit.
    GPIO.output(buzzer, GPIO.HIGH if trans == 'PNP' else GPIO.LOW)
    time.sleep(1 * unit)


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
            message = input("What is your message: ")

            # translate the input into morse code
            code = encode(message)
            print(code)

            # play the dots and dashes on the buzzer
            for c in code:
                if c == '.':
                    play_dot()
                elif c == '-':
                    play_dash()
                else:
                    try:
                        time.sleep(int(c) * unit)
                    except ValueError:
                        time.sleep(7 * unit)

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
