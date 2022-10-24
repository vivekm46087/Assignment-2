from itertools import count
from urllib import response
from flask import Flask, request
import requests

app = Flask(__name__)
app.debug = True

@app.route('/')
def student_id():
    return '{"studentId":200535447}'

@app.route('/webhook', methods=["POST", "GET"])

def covid_statistics_api():
    body = request.json
    country = body["queryResult"]["parameters"]["country"]

    api_url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total"

    querystring = {"country":country}

    headers = {
        "X-RapidAPI-Key": "296c5226dbmshf949b3eecce99c1p15a05fjsnede441773157",
        "X-RapidAPI-Host": "covid-19-coronavirus-statistics.p.rapidapi.com"
    }

    response = requests.get(api_url, paramgs=querystring, headers=headers )
    r = response.json()
    deaths = str(r["data"]["deaths"])
    confirmed = str(r["data"]["confirmed"])
    lastChecked =  str(r["data"]["lastChecked"])
    lastReported =  str(r["data"]["lastReported"])
    #fulfilment message

    fulfillment_reply = '{"fulfillmentMessages": [ {"text": {"text": ["The Covid statistics for ' + country + " are: \n\t Deaths:" + deaths + "\n\t Confirmed:" + confirmed + "\n\t Last Reported:" + lastReported + ":" +  '\n\t Last Checked: ' + lastChecked+  '"]}}]}'

    return fulfillment_reply




