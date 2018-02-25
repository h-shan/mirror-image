import os
import requests

GREETING_INTENT = "Greeting"
SUMMARY_INTENT = "Summary"
OPINION_INTENT = "Opinion"
COMMAND_INTENT = "Command"
EXCLAIM_INTENT = "Exclaim"
DESCRIP_INTENT = "Description"
DESIRE_INTENT = "Desire"
END_INTENT = "End"
NONE_INTENT = "None"

SELF = "Self"
MOOD = "Mood"
DAY = "Day"
TIME = "Time"
ADJ = "Adjective"

LUIS_KEY = None
APP_ID = None

if 'LUIS_KEY' in os.environ:
    LUIS_KEY = os.environ['LUIS_KEY']
    APP_ID = os.environ['APP_ID']
else:
    import key
    LUIS_KEY = key.LUIS_KEY
    APP_ID = key.APP_ID

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': LUIS_KEY,
}

def request(text):
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
        r = requests.get('https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/' + APP_ID, headers=headers, params=params)
        return r.json()

    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
