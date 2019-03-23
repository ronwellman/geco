# Binary Display Lab
This lab is intended to guide the students towards figuring out the components
of the lab rather than provide to them working code.  Students are not
expected to be able to write this from scratch but provide input as we explore
the Raspberry Pi (RPi) Command Line Interface (CLI) and the python code
required to complete it.  `

This lab is built to continue to re-enforce the use of loops and exception
handling.  

## Wire up the Circuit
Mentors should assist the student's in wiring up the circuit to ensure they
don't damage the RPi.  This is done while the RPi is powered off for safety and
once verified, the RPi can be turned on.  See the included diagram
[binary_display.png](./fritzing/binary_display.png) for correct wiring of the circuit.

The LED's will represent the number in binary. Least Significant Bit (LSB) is
the rightmost LED and Most Significant Bit (MSB) is the leftmost bit.

## Getting the files
Now make the binary_display pseudocode available to the students via python:

```bash
cd binary_display
python3 -m http.server
```

This should launch a web server on port 8000.  Students should go to their
respective CLIs on their RPi and pull down the pseudocode.  The projects
directory may have been created in a previous lab.

```
cd ~/
mkdir projects
cd projects
mkdir binary_display
cd binary_display
wget://MENTORS_RPI_IP:8000/psuedocode.py
```

## Writing binary_display.py
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
Once the students have completed binary_display.py with the mentor, it is time 
to try it out.  Some IDEs have a built-in "run" button.  However, encourage the
students to return to the command line and execute it from there. There will no
doubt be typos in the student's code.  Mentors should guide the student to
interpret the errors and make the appropriate fixes.

If they have to open a new terminal.
```bash
cd ~/projects/binary_display/
```

Execute the program.
```
./binary_display.py
```

In order to stop the program, students will have to hit `ctrl-c`.
