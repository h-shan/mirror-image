import requests
import key
import random

GREETING_TYPE = "Greeting"
SUMMARY_TYPE = "Summary"
SELF = "Self"
MOOD = "Mood"
DAY = "Day"
TIME = "Time"
ADJ = "Adjective"
OPINION_TYPE = "Opinion"

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': key.LUIS_KEY,
}

def make_response(result):
    intent = result["topScoringIntent"]["intent"]
    entities = result["entities"]
    if GREETING_TYPE in intent:
        poss = ["Hello", "How are you?", "Hi"]
        return random.choice(poss)
    elif SUMMARY_TYPE in intent:
        if SELF in intent:
            for entity in entities:
                if entity["type"] == MOOD:
                    return "Why are you " + entity["entity"] + "?"
        elif DAY in intent:
            time = ""
            adj = ""
            for entity in entities:
                if entity["type"] == TIME:
                    time = entity["entity"] 
                elif entity["type"] == ADJ:
                    adj = entity["entity"] 
            if time != "" and adj != "":
                return "Why was " + time + " " + adj + "?"
        return "Tell me more"
    elif OPINION_TYPE in intent:
        pos = ["I agree", "You're right", "I think so too"]
        neg = ["I disagree"]
        return random.choice(pos)
    else:
        return ""

def request_luis(text):
    params ={
        # Query parameter
        'q': text,
        # Optional request parameters, set to default values
        'timezoneOffset': '0',
        'verbose': 'false',
        'spellCheck': 'false',
        'staging': 'false',
    }

    try:
        r = requests.get('https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/' + key.APP_ID ,headers=headers, params=params)
        resp = make_response(r.json())
        print(r.json())
        if resp == "":
            return r.json()
        else:
            return resp

    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))