# GECO
This is a repository for various GECO girls projects.

## Projects
1. [rpi_poll.py](./rpi_poll.py)

   This script is used to log into an old D-Link DGL-4500 circa 2013 wireless router using the requests library.  It then scrapes the wireless hosts status screen extracting the host information via BeautifulSoup.  Finally, it then displays the results using the curses library.  This makes it easy to find all of the expected Raspberry Pi's (RPIs) as they connect to the access point.

### Clone repository

   ```bash
   git clone https://github.com/ronwellman/geco.git
   cd geco
   ```

### Virtual Environment

#### PIPENV
   A [Pipfile](./Pipfile) and [Pipfile.lock](./Pipfile.lock) was also included.  Pipenv is another way to setup virtual environments and get the required modules installed. 

   ```bash
   pipenv install
   pipenv shell
   python3 rpi_poll.py
   ```

   To deactivate:

   ```bash
   exit
   ```

#### PIP

   If pipenv isn't your cup of tea, a [requirements.txt](./requirements.txt) file was included to replicate the environment using PIP. 

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip3 install -r requirements.txt
   python3 rpi_poll.py
   ``` 
   
   To deactivate:
   ```bash
   deactivate
   ```
 
2. [RPi.tex](./doc/RPi.tex)

   This LATEX document was using in generating a how-to for setting up ssh and VNC on a Raspberry Pi.  It then shows how to install Real-VNC on a Windows, OSX, and Linux box to connect to the RPI.  This was written and compiled with TeXstudio and based off of a template from [http://www.LaTeXTemplates.com](http://www.LaTeXTemplates.com).

