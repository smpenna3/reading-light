from flask import Flask, render_template, request, abort, jsonify, url_for, redirect
from flask_socketio import SocketIO
from flask_cors import CORS
import os
import time
import traceback

#################################################################################################
debugSet = True
external = False

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, async_mode='threading')


@app.route('/')
def home():
    return render_template('home.html')


@socketio.on('on', namespace='/led')
def on():
    print("Turn on")


@socketio.on('off', namespace='/led')
def off():
    print("Turn off")


if(__name__ == '__main__'):
    if(external):
        socketio.run(app, debug=debugSet, host='0.0.0.0')
    else:
        socketio.run(app, debug=debugSet)