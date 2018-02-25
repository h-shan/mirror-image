from datetime import datetime
import sys
import json
import os

from flask import Flask, request
import requests

from chat_util import text_analytics, response

app = Flask(__name__)

prev_senti = 0.5

@app.route('/test', methods=['GET'])
def test():
    return 'TEST SUCCESS', 200

# @app.route('/', methods=['GET'])
# def verify():
#     # when the endpoint is registered as a webhook, it must echo back
#     # the 'hub.challenge' value it receives in the query arguments
#     if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
#         if not request.args.get("hub.verify_token") == os.environ["VERIFY_TOKEN"]:
#             return "Verification token mismatch", 403
#         return request.args["hub.challenge"], 200

#     return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():
    return 'TEST SUCCESS 2', 200
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


def send_message(recipient_id, message_text):

    log("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text))

    params = {
        "access_token": os.environ["PAGE_ACCESS_TOKEN"]
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": message_text
        }
    })
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        log(r.status_code)
        log(r.text)


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
    app.run(debug=True)
