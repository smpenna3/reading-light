from flask import Flask, render_template, request, abort, jsonify, url_for, redirect
from flask_socketio import SocketIO
from flask_cors import CORS
import os
import time
import traceback

# Import the LED Control
from LED import LED

#################################################################################################
debugSet = True
external = False
port = ''

#################################################################################################


app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, async_mode='threading')


# Setup LED
led = LED(port)


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


if(__name__ == '__main__'):
    if(external):
        socketio.run(app, debug=debugSet, host='0.0.0.0')
    else:
        socketio.run(app, debug=debugSet)