from flask import Flask, render_template, request, abort, jsonify, url_for, redirect
from flask_socketio import SocketIO
import os
import time
import traceback
import argparse

# Import the LED Control
from LED import LED, LED_test

# Parse Arguments
parser = argparse.ArgumentParser(description="Reading Light")
parser.add_argument('-a', '--arduino', action='store_false')
args = parser.parse_args()

#################################################################################################
debugSet = False
external = True
arduino_port = '/dev/ttyACM0'
port = 8000

#################################################################################################


app = Flask(__name__)
socketio = SocketIO(app, async_mode='threading')


# Setup LED
if(args.arduino):
    led = LED(arduino_port)
else:
    led = LED_test()


@app.route('/')
def home():
    return render_template('home.html')


@socketio.on('on', namespace='/led')
def on():
    print("Turn on")
    led.color(255, 20, 20)


@socketio.on('off', namespace='/led')
def off():
    print("Turn off")
    led.off()


@socketio.on('rgb', namespace='/led')
def rgb(colors):
    print("RGB: " + str(colors))
    red = colors.get('red', 0)
    green = colors.get('green', 0)
    blue = colors.get('blue', 0)
    led.color(red, green, blue)


if(__name__ == '__main__'):
    if(external):
        socketio.run(app, debug=debugSet, port=port, host='0.0.0.0')
    else:
        socketio.run(app, port=port, debug=debugSet)
