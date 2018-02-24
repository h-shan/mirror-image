import requests
import os

SUBSCRIPTION_KEY = None
if 'SUBSCRIPTION_KEY' in os.environ: # running on heroku
    SUBSCRIPTION_KEY = os.environ['SUBSCRIPTION_KEY']
else:
    import key
    assert key.SUBSCRIPTION_KEY
    SUBSCRIPTION_KEY = key.SUBSCRIPTION_KEY

text_analytics_base_url = "https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/"
sentiment_api_url = text_analytics_base_url + "sentiment"
key_phrase_api_url = text_analytics_base_url + "keyPhrases"

#user_input = "I had a wonderful experience! The rooms were wonderful and the staff was helpful."

def analyze(user_input):
    documents = {'documents' : [
        {'id': '1', 'language': 'en', 'text': user_input}
    ]}

    headers = {"Ocp-Apim-Subscription-Key": SUBSCRIPTION_KEY}
    response = requests.post(sentiment_api_url, headers=headers, json=documents)
    sentiments = response.json()
    #print("Sentiment:", sentiments["documents"][0]["score"])

    response = requests.post(key_phrase_api_url, headers=headers, json=documents)
    key_phrases = response.json()
    #print("Key Phrases:", key_phrases["documents"][0]["keyPhrases"])
    return sentiments["documents"][0]["score"], key_phrases["documents"][0]["keyPhrases"]
