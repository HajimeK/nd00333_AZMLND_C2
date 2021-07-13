import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here

data = {"data":
        [
          {
            "age": "17",
            "campaign": "1",
            "cons.conf.idx": "-46.2",
            "cons.price.idx": "92.893",
            "contact": "cellular",
            "day_of_week": "mon",
            "default": "no",
            "duration": "971",
            "education": "university.degree",
            "emp.var.rate": "-1.8",
            "euribor3m": "1.299",
            "housing": "yes",
            "job": "blue-collar",
            "loan": "yes",
            "marital": "married",
            "month": "may",
            "nr.employed": "5099.1",
            "pdays": "999",
            "poutcome": "failure",
            "previous": "1"
          }
      ]
    }


body = str.encode(json.dumps(data))

url = 'http://d8e9f6ad-4112-4417-97c0-01b4246b284a.japaneast.azurecontainer.io/score'
api_key = 'sYDHOfPPfLTb0w5gDucnNQfT8VinfhBf' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))
