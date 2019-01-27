#!/usr/bin/env python3

from morse_code import *
import RPi.GPIO as GPIO
import time

buzzer = 17
'''
There are rules to help people distinguish dots from dashes in Morse code.
The length of a dot is 1 time unit.
A dash is 3 time units.
The space between symbols (dots and dashes) of the same letter is 1 time unit.
The space between letters is 3 time units.
The space between words is 7 time units.
'''

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buzzer, GPIO.OUT)
    GPIO.output(buzzer, GPIO.HIGH)


def teardown():
    GPIO.cleanup()


def play_dot():
    GPIO.output(buzzer, GPIO.LOW)
    time.sleep(.1)
    GPIO.output(buzzer, GPIO.HIGH)
    time.sleep(.3)


def play_dash():
    GPIO.output(buzzer, GPIO.LOW)
    time.sleep(.3)
    GPIO.output(buzzer, GPIO.HIGH)
    time.sleep(.3)


def main():
    try:
        while True:
            message = input("What is your message: ")
            code = encode(message)
            print(code)

            for c in code:
                if c == '.':
                    play_dot()
                elif c == '-':
                    play_dash()
                else:
                    time.sleep(.4)
    except KeyboardInterrupt:
        print()
        return 0

        



if __name__ == "__main__":
    setup()
    main()
    teardown()
