from flask import Flask, render_template, request, abort, jsonify, url_for, redirect
from flask_socketio import SocketIO
import os
import time
import traceback

#################################################################################################
debugSet = False
external = False

app = Flask(__name__)
socketio = SocketIO(app, async_mode='threading')


@app.route('/')
def home():
    return render_template('home.html')


if(__name__ == '__main__'):
    if(external):
        socketio.run(app, debug=debugSet, host='0.0.0.0')
    else:
        socketio.run(app, debug=debugSet)