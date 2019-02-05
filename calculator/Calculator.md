# Calculator Lab
This lab is intended to guide the students towards figuring out the components
of the lab rather than provide to them working code.  Students are not
expected to be able to write this from scratch but provide input as we explore
the Raspberry Pi (RPi) Command Line Interface (CLI) and the python code
required to complete it.  `

Specifically, this lab is to continue to re-enforce the use of for loops but
also relies heavily on index values when working with lists.

## Wire up the Circuit
Mentors should assist the student's in wiring up the circuit to ensure they
don't damage the RPi.  This is done while the RPi is powered off for safety and
once verified, the RPi can be turned on.  See the included diagram
[calculator.png](./fritzing/calculator.png) for correct wiring of the circuit.

The LED's will represent the number in binary.  Students set and clear the
bits via the rightmost four buttons.  When the leftmost button is pressed, it
progresses through three modes: 

*  Mode 0 - Accept first number
*  Mode 1 - Accept second number
*  Mode 2 - Display the sum

## Getting the files
Now make the calculator pseudocode available to the students via python:

```bash
cd calculator
python -m http.server
```

This should launch a web server on port 8000.  Students should go to their
respective CLIs on their RPi and enter the following:

```
cd ~/
mkdir projects
cd projects
mkdir calculator
cd calculator
wget://MENTORS_RPI_IP:8000/psuedocode.py
```

## Writing calculator.py
Have the students open the pseudocode.py file in the editor or Integrated 
Development Environment (IDE) of their choice.  They can use Geany, Python 
Idle, Thonny, gedit, or any of the other included text editors or IDEs.  My 
preferred editor is VIM but I wouldn't recommend having the student's code in 
it unless they are already used to the CLI interface.

Again, students are not expected to know the exact syntax to accomplish this
lab.  However, encourage them to talk through what they are thinking and then
direct them to the syntax.  Mentors can also bring up a the python interpreter
to walk through elements of the code to demonstrate concepts like for loops and
using index values with lists.

## Executing the program
Once the students have completed calculator.py with the mentor, its time to try
it out.  Some IDEs have a built-in "run" button.  However, encourage the
students to return to the command line and execute it from there.

If they have to open a new terminal.
```bash
cd ~/projects/calculator/
```

Execute the program.
```
./calculator.py
```

In order to stop the program, students will have to hit `ctrl-c`.
