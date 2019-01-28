# Morse Code Generator
In this lab, we build a tool that takes text as input, translates it into morse
code, and plays it over a buzzer connected to the Raspberry Pi (RPi).

This lab is intended to guide the students towards figuring out the components
of the lab rather than provide to them working code.  Students are not
expected to be able to write this from scratch but provide input as we explore
the Raspberry Pi (RPi) Command Line Interface (CLI) and the python code
required to complete it.

Additionally, morse_code.py has been configured as a package for the students
to import as they code up generator.py.  They will be required to wire up the
circuit and code the generator.py script along with the mentor.  They should
not have to touch morse_code.py directly.

## Morse Code Lab
This lab was built for the GECO girls to touch on the following principles:

  * Basic Electionics:
    * DC circuits
    * Transistors
  * Linux CLI commands:
    * cd
    * mkdir
    * wget
    * tar
    * gunzip
    * touch
    * chmod
  * Python fundamentals:
    * for loops
    * if statements
    * RPi.GPIO
    * importing packages
    * exception handling

## Hardware
All of the below parts are part of the Sunfounder Super Kit v2 for Raspberry Pi
(RPi) except for the RPi itself. 

  * RPi
  * Breadboard
  * 1k Resister
  * Buzzer
  * PNP Transister (8550)
  * ~ 6 Jumper wires

## Software
With the exception of this project's files, no other software is required
outside of the standard Raspian image for the RPi.  generator.py was written 
by Joshua Wellman and morse_code.py was copied from Geeks for Geeks.  See 
attribution and licensing below.

## Attribution
The morse_code.py software was copied from: 
> https://www.geeksforgeeks.org/morse-code-translator-python/

## Licensing
Geeks for Geeks is covered by the following license: 
> Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)  
> https://creativecommons.org/licenses/by-sa/4.0/

This also means that the entirety of this morse code generator project is also covered by the same license.
