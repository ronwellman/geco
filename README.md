# GECO
This is a repository for various GECO girls projects.

## Projects
1. [rpi_poll.py](./rpi_poll.py)

   This script is used to log into an old D-Link DGL-4500 circa 2013 wireless router using the requests library.  It then scrapes the wireless hosts status screen extracting the host information via BeautifulSoup.  Finally, it then displays the results using the curses library.  This makes it easy to find all of the expected Raspberry Pi's (RPIs) as they connect to the access point.

   A [requirements.txt](./requirements.txt) file was included to replicate the environment I was running when I wrote it.

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip3 install -r requirements.txt
   chmod u+x rpi_poll.py
   ./rpi_poll.py
   ```   

2. [RPi.tex](./doc/RPi.tex)

   This LATEX document was using in generating a how-to for setting up ssh and VNC on a Raspberry Pi.  It then shows how to install Real-VNC on a Windows, OSX, and Linux box to connect to the RPI.  This was written and compiled with TeXstudio and based off of a template from [http://www.LaTeXTemplates.com](http://www.LaTeXTemplates.com).

