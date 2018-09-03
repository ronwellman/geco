#!/usr/bin/env python3
import curses
from curses import wrapper
import requests
from requests.exceptions import ConnectionError, Timeout
from hashlib import md5
import re
from bs4 import BeautifulSoup as bs
import time


class InvalidCredentials(Exception):
    '''Thrown if login doesn't work as excpected.'''
    pass


def build_payload(text):
    '''
    The below procedures generate the required payload to login to the DGL-4500
    Gaming router (Firmware: 1.24WW,  2013/08/02) used in the geco girls lab.
    '''
    # auth_id is unique every login
    m = re.search('auth_id=(\w+)', text)
    auth_id = m.group(1)

    # salt is unique every login
    m = re.search('var salt = "(\w+)"', text)
    salt = m.group(1)

    password = salt + 'just4mentors'
    password += chr(1) * (64 - len(password))
    hash = md5(password.encode('utf-8')).hexdigest()

    hash = salt + hash
    payload = {'hash': hash, 'auth_code': '', 'auth_id': auth_id}
    return payload


def get_page(s, URL, payload=None):
    '''
    General purpose function for executing a get request on the session given a
    URL and potentially a payload.  Rather than passing the payload across, it
    is used to build a custom get string.
    '''
    authdata = ''

    if payload is not None:
        authdata = '?' + 'hash=' + payload['hash'] + '&' +\
            'auth_code=&auth_id=' + payload['auth_id']

    r = s.get(URL + authdata, timeout=.25)

    return r


def update_clients():
    '''
    Builds a requests session object and attempts to query the router for the
    wireless clients.
    '''
    URL = 'http://192.168.0.1/'
    POST_URL = 'http://192.168.0.1/post_login.xml'

    with requests.Session() as s:
        # initial page holds aspects needed to generate login payload
        r = get_page(s, URL)
        payload = build_payload(r.text)
        r = get_page(s, POST_URL, payload)
        if 'Basic/Internet.shtml' in r.text:
            r = get_page(s, URL + 'wifi_assoc.xml')
        else:
            raise InvalidCredentials

    if 'assoc' in r.text:
        return r.text

    return None


def main(stdscr):
    rpi = {'B8:27:EB:0A:29:BE': {'NAME': 'raspberrypi', 'IP': ''},
           'B8:27:EB:6C:34:70': {'NAME': 'applepi', 'IP': ''},
           'B8:27:EB:BD:81:35': {'NAME': 'strawberrypi', 'IP': ''},
           '00:0f:60:08:1f:04': {'NAME': 'cherrypi', 'IP': ''},
           'B8:27:EB:4A:AA:65': {'NAME': 'bannapi', 'IP': ''},
           'B8:27:EB:01:FB:49': {'NAME': 'lemonpi', 'IP': ''},
           'B8:27:EB:DC:69:19': {'NAME': 'pecanpi', 'IP': ''},
           'B8:27:EB:60:CB:0B': {'NAME': 'blueberrypi', 'IP': ''},
           'B8:27:EB:F2:28:37': {'NAME': 'blackberrypi', 'IP': ''},
           'B8:27:EB:B6:D2:E6': {'NAME': 'keylimpi', 'IP': ''},
           'B8:27:EB:E7:9D:3A': {'NAME': 'cutiepi', 'IP': ''}}

    # initialize ncurses
    stdscr = curses.initscr()
    curses.start_color()
    stdscr.clear()
    curses.cbreak()
    curses.noecho()

    # how long with getch wait for an input (10ths of a second)
    curses.halfdelay(50)

    # setup alternating colors
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_GREEN)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_RED)

    loop = True
    while(loop):
        line = 0
        clients = None
        soup = None

        stdscr.move(0, 0)
        stdscr.clrtoeol()
        try:
            # get updated list of clients
            clients = update_clients()
            stdscr.addstr(line, 0, f'Access Point: GOOD', curses.color_pair(3))
        except (ConnectionError, Timeout) as e:
            stdscr.addstr(line, 0, f'Access Point: ERROR Connecting',
                          curses.color_pair(4))
        except InvalidCredentials:
            stdscr.addstr(line, 0, f'Access Point: Invalid Login Credentials',
                          curses.color_pair(4))

        line += 2

        if clients:
            soup = bs(clients, 'html.parser')

        # load the dictionary with wireless RPI entries
        if soup:
            for entry in soup.find_all('assoc'):
                mac = entry.mac.text
                mac = ':'.join((mac[x:x+2] for x in range(0, 12, 2)))
                if mac in rpi:
                    rpi[mac]['IP'] = entry.ip_address.text

        max_name_size = max((len(v['NAME']) for v in rpi.values()))
        max_ip_size = max((len(x["IP"]) for x in rpi.values()))

        col_1 = 0

        if max_name_size < 12:
            col_2 = col_1 + 17
        else:
            col_2 = col_1 + max_name_size + 5

        col_3 = col_2 + 22

        if max_ip_size < 10:
            col_4 = col_3 + 10
        else:
            col_4 = col_3 + max_ip_size

        top_bar = "RASPBERRY PI" + " " * (col_2 - 12)
        top_bar += "MAC ADDRESS" + " " * (col_3 - col_2 - col_1 - 11)
        top_bar += "IP ADDRESS"

        stdscr.addstr(line, col_1, top_bar, curses.A_UNDERLINE)
        line += 1

        for k, v in sorted(rpi.items(), key=lambda x: x[1]['NAME']):
            if line % 2 == 0:
                color = 1
            else:
                color = 2
            name = v['NAME']
            mac = k
            ip = v['IP']

            stdscr.addstr(line, col_1, name, curses.color_pair(color))
            stdscr.addstr(line, col_1 + len(name),
                          ' ' * (col_2 - (col_1 + len(name))),
                          curses.color_pair(color))
            stdscr.addstr(line, col_2,  mac, curses.color_pair(color))
            stdscr.addstr(line, col_2 + 17,
                          ' ' * 5,
                          curses.color_pair(color))
            stdscr.addstr(line, col_3, ip, curses.color_pair(color))
            stdscr.addstr(line, col_3 + len(ip),
                          ' ' * (col_4 - (col_3 + len(ip))),
                          curses.color_pair(color))
            line += 1

        stdscr.addstr(line + 2, 0, f'Last Poll: {time.ctime()}')
        stdscr.addstr(line + 4, 0, "HIT <Q> TO QUIT")
        stdscr.refresh()

        c = stdscr.getch()
        if c == 113 or c == 81:
            loop = False

    return 0


wrapper(main)
