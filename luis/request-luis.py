import requests
import key

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': key.LUIS_KEY,
}

params ={
    # Query parameter
    'q': 'who is the coolest dog in puppyland?',
    # Optional request parameters, set to default values
    'timezoneOffset': '0',
    'verbose': 'false',
    'spellCheck': 'false',
    'staging': 'false',
}

try:
    r = requests.get('https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/' + key.APP_ID ,headers=headers, params=params)
    print(r.json())

except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))