# Calculator
In this lab, we build a calculator that can add two four-bit numbers together 
and display the results on five LEDs.

This lab is intended to guide the students towards figuring out the components
of the lab rather than provide to them working code.  Students are not
expected to be able to write this from scratch but provide input as we explore
the Raspberry Pi (RPi) Command Line Interface (CLI) and the python code
required to complete it.

On the surface this lab it not overly difficult.  However, it will challenge
students to think about how to line up the buttons, the LEDs, and the 
calculated values while progressing through the lab.  This can be accomplished 
in a number of ways and students are encouraged to tackle sections of the code 
on their own to feel the difficulty in balancing this.  However, mentors should
walk through the solution given as an example method and talk about it 
conceptually rather than getting deep into the weeds of the particular python 
syntax.  Methodology and thought processes should be more important than the 
actual syntax. 

Specifically, this lab is built to continue to re-enforce the use of loops and
thought processes.  However, it also relies heavily on the use of index values 
when working with lists.

## Calculator Lab
This lab was built for the GECO girls to touch on the following principles:

  * Basic Computing
    * Binary Number System
  * Basic Electronics:
    * DC circuits
  * Linux CLI commands:
    * cd
    * mkdir
    * wget
    * chmod
  * Python fundamentals:
    * for loops
    * if statements
    * RPi.GPIO
    * Lists
    * Modulus Operator

## Hardware

  * RPi
  * Breadboard
  * 5 x 470 Ohm Resister
  * 5 x LED
  * 5 x Pushbutton Switch
  * ~ 16 Jumper wires

## Software
With the exception of this project's files, no other software is required
outside of the standard Raspian image for the RPi.  
