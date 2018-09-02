from datetime import datetime
import sys
import json
import os

from flask import Flask, request
import requests

from chat_util import text_analytics, response

app = Flask(__name__)

prev_senti = 0.5


@app.route('/', methods=['POST'])
def webhook():
    # endpoint for processing incoming messaging events

    data = request.get_json()
    log(data)  # you may not want to log every incoming message in production, but it's good for testing

    response_message = ''
    if data and 'message' in data:
        message_text = data['message']  # the message's text
        cur_senti, keyword = text_analytics.analyze(message_text)
        
        global prev_senti
        response_message = response.respond(cur_senti, prev_senti, keyword, message_text)
        prev_senti = cur_senti
    else:
        log('Invalid json')
    return response_message, 200


def log(msg):  # simple wrapper for logging to stdout on heroku
    try:
        if type(msg) is dict:
            msg = json.dumps(msg)
        else:
            pass
            #msg = str(msg).format(*args, **kwargs)
        print(("{}: {}".format(datetime.now(), msg)))
    except UnicodeEncodeError:
        pass  # squash logging errors in case of non-ascii text
    sys.stdout.flush()


if __name__ == '__main__':
    app.run(debug=True, port=6000)
