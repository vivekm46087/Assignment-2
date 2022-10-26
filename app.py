from flask import Flask, request
import requests

app = Flask(__name__)
app.debug = True

@app.route('/')
def student_id():
    return '{"studentId":200535447}'

@app.route('/webhook', methods=["POST", "GET"])

def covid_statistics_api():
    body = request.get_json(force=True)
    country_name = body["queryResult"]["parameters"]["geo-country"]

    api_url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total"

    querystring = {"country":country_name}

    headers = {
        "X-RapidAPI-Key": "296c5226dbmshf949b3eecce99c1p15a05fjsnede441773157",
        "X-RapidAPI-Host": "covid-19-coronavirus-statistics.p.rapidapi.com"
    }

    response = requests.get(api_url, params=querystring, headers=headers )
    r = response.json()
    deaths = str(r["data"]["deaths"])
    confirmed = str(r["data"]["confirmed"])
    # lastChecked =  str(r["data"]["lastChecked"])
    # lastReported =  str(r["data"]["lastReported"])
    #fulfilment message
    

    fulfillment_reply = '{"fulfillmentMessages": [ {"text": {"text": ["The Covid statistics for ' + country_name + " are: \n\t Deaths:" + deaths + "\n\t Confirmed:" + confirmed + "\n\t Last Reported:"  + ":" +  '\n\t Last Checked: ' +  '"]}}]}'

    return fulfillment_reply




