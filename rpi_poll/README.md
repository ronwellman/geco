# RPI_POLL

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

   A [run_rpi.sh](./run_rpi.sh) shell script has been included to make running the script within the virtual environment.
   
   ```bash
   chmod u+x run_rpi.sh
   ./run_rpi.sh
   ```

   This will run [rpi_poll.py](./rpi_poll.py) within the virtual environment.

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

