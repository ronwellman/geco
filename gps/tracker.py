#!/usr/bin/env python3
import os
import json
import threading
import atexit
from flask import Flask, render_template, url_for
from gps3 import gps3
import time

POOL_TIME = 1
dataLock = threading.Lock()
gps_thread = threading.Thread()

# create and configure the app
app = Flask(__name__, instance_relative_config=True)
# app.config.from_pyfile('config.py', silent=True)
app.config.from_object('config')

gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()
keep_looping = True

# ensure the instance folder exists
# I don't think I need this
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

def interrupt():
    global keep_looping
    keep_looping = False
    time.sleep(2)
    gps_socket.close()

def poll_gps():
    # global gps_socket
    for new_data in gps_socket:
        if new_data:
            data_stream.unpack(new_data)
            if not keep_looping:
                break

# @app.before_first_request
def activate_gps():
    gps_socket.connect()
    gps_socket.watch()
    global gps_thread
    gps_thread = threading.Thread(target=poll_gps)
    gps_thread.start()

# a simple page that says hello
@app.route('/')
def map_page():

    data = {'lat': data_stream.TPV['lat'], 'lon': data_stream.TPV['lon'], 'marker': url_for('static', filename='marker.png')}
    return render_template('index.html', data=json.dumps(data), api_key=app.config['MAPS_API_KEY'])

activate_gps()
atexit.register(interrupt)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
