# Morse Code Lab
This lab is intended to guide the students towards figuring out the components
of the lab rather than provide to them working code.  Students are not
expected to be able to write this from scratch but provide input as we explore
the Raspberry Pi (RPi) Command Line Interface (CLI) and the python code
required to complete it.  `

Additionally, morse_code.py has been configured as a package for the students
to import as they code up generator.py.  They will be required to wire up the
circuit and code the generator.py script along with the mentor.  They should
not have to touch morse_code.py directly.

## Wire up the Circuit
Mentors should assist the student's in wiring up the circuit to ensure they
don't damage the RPi.  This is done while the RPi is powered off for safety and
once verified, the RPi can be turned on.  See the included diagram for correct
wiring of the circuit.

### Transistors
Transistors essentially allow a small amount of current to trigger and allow
the flow of a larger amount of current.  In this way, they are often described 
as amplifying the current.  They are one of the most important components 
in any modern circuit today.  Although the students only have one in their
circuit, the RPi is composed of potentially billions of transistors when you
factor in the processor, RAM, and additional chips/peripherals because they are
integrated at the nano-meter scale.

The transistor the students will be using is a PNP transistor.  It has three 
legs composed of the emitter, base, and collector.  With this transistor,
control current flows from the emitter to the base when the voltage on the 
base is lower than than the voltage applied to the emitter.  In this mode, the 
transistor is on and a larger current flows from the emitter to the collector 
allowing the buzzer will sound.  When the voltage on the base is higher 
than that on the emitter, control current does not flow and the transistor is 
shut down.  In this mode current cannot flow from emitter to collector and
therefore the buzzer will not sound. 

### Buzzer
The buzzer we will be utilizing is an active buzzer.  This means that it
contains the necessary oscillators to make sounds.  As such, the sound cannot
be varied in pitch.

## Getting the files
Mentors should tar and gzip the morse_code package and host it for the students
to download.  It is assumed, this package is already on the mentor RPi at the
following location: 

```
/home/pi/projects/morse_code/
/home/pi/projects/morse_code/morse_code/
/home/pi/projects/morse_code/morse_code/morse_code.py
/home/pi/projects/Morse_code/morse_code/__init__.py
```

```bash
cd ~/projects/morse_code/
tar -cf morse_code.tar morse_code/
gzip morse_code.tar
```

Now make morse_code.tar.gz available to the students via python:

```bash
python -m http.server
```

This should launch a web server on port 8000.  Students should go to their
respective CLIs on their RPi and enter the following:

```
cd ~/
mkdir projects
cd projects
wget://MENTORS_RPI_IP:8000/morse_code.tar.gz
gunzip morse_code.tar.gz
tar -xf morse_code.tar
```

## Verifying the package
Now the students have the lab on their RPis unzipped and ready to use.  To test
it out, have the students open python from their shell and import the package.

```bash
python3
```

```python
from morse_code import encode

print(encode("this is a test"))
quit()
```

## Morse Code
Per Wikipedia: Morse code is a character encoding scheme used in 
telecommunication that encodes text characters as standardized sequences of two
different signal durations called dots and dashes or dits and dahs (dots and
dashes). Morse code is named for Samuel F. B. Morse, an inventor of the 
telegraph.

Essentially, we'll be using these dots and dashes to convey a message through
the buzzer's connected to our RPi.

The dot duration is the basic unit of time measurement in Morse code 
transmission.

There are rules to help people distinguish dots from dashes in Morse code.
The length of a dot is 1 time unit.
A dash is 3 time units.
The space between symbols (dots and dashes) of the same letter is 1 time unit.
The space between letters is 3 time units.
The space between words is 7 time units.
http://www.codebug.org.uk/learn/step/541/morse-code-timing-rules/

## Writing generator.py
The students should see a string of dots, dashes, and numbers printed to the
screen.  This is the text that will be parsed to activate the buzzer. Have the
student create the generator.py file and set it as executable.
```bash
touch generator.py
chmod u+x generator.py
```

Have the students open the file in the editor or Integrated Development
Environment (IDE) of their choice.  They can use Geany, Python Idle, Thonny,
gedit, or any of the other included text editors or IDEs.  My preferred editor 
is VIM but I wouldn't recommend having the student's code in it unless they are
already used to the CLI interface.

It is suggested to write out some pseudo code like the following, and then
as you discuss each, circle back and fill in the correct python.

```
import package

initialize RPi (setup)

restore RPi(cleanup)

play_dot
play_dash

Main Loop
    prompt for input
    encode the input into morse code
    send the dots and dashes to the buzzer
    allow the user to quit
```

Below is the a working generator.py file utilizing GPIO 17 on the RPi with a
8550 PNP transistor:

```python3
#!/usr/bin/env python3

from morse_code import encode
import RPi.GPIO as GPIO
import time

buzzer = 17
unit = .2
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
    GPIO.output(buzzer, GPIO.HIGH)


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
    GPIO.output(buzzer, GPIO.LOW)
    time.sleep(1 * unit)

    # The space between symbols of the same letter is 1 time unit.
    GPIO.output(buzzer, GPIO.HIGH)
    time.sleep(1 * unit)


def play_dash():
    '''
    play_dash() -> NoneType

    Play a morse code dash (long).
    '''
    # A dash is 3 time units.
    GPIO.output(buzzer, GPIO.LOW)
    time.sleep(3 * unit)

    # The space between symbols of the same letter is 1 time unit.
    GPIO.output(buzzer, GPIO.HIGH)
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
```

## Executing the program
Once the students have completed generator.py with the mentor, its time to try
it out.  Some IDEs have a built-in "run" button.  However, encourage the
students to return to the command line and execute it from there.

If they have to open a new terminal.
```bash
cd ~/projects/morse_code/
```

Execute the program.
```
./generator.py
```

In order to stop the program, students will have to hit `ctrl-c`.
