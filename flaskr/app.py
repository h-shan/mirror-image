import os
import sys
import json
from datetime import datetime

import requests
from flask import Flask, request, session, redirect, url_for, render_template, flash, make_response

app = Flask(__name__)
messages = [] # message = [['sender', 'msg', 'time']]

@app.route('/', methods=['GET'])
def chat():
    return render_template('index.html', messages=messages)


@app.route('/', methods=['POST'])
def send():
    message = request.form['msg']
    if message != "":
        messages.append(['You', message, datetime.now().strftime("%h. %d, %Y. %I:%M:%S %p")])
        send_message(message)
    return redirect(url_for('chat'))

def send_message(message_text):
    pass

if __name__ == '__main__':
    app.run(debug=True)
