import pandas as pd
import json
import requests
import json

import pymongo
from pymongo import MongoClient
from flask import Flask, request, jsonify, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World'

@app.route('/getFromMongo', methods=["GET"])
def getFromMongo():
    client=pymongo.MongoClient("mongodb+srv://siberian:siberian@cluster0.jrgmw.mongodb.net/parcial?retryWrites=true&w=majority")
    db=client.test
    mydb=client["parcial"]
    mycol=mydb["parcial"]
    
    return mycol.find_one()
    

    ####################################
##    url = "https://data.mongodb-api.com/app/data-lrgqy/endpoint/data/beta/action/findOne"
##    payload = json.dumps({
##        "collection": "parcial",
##        "database": "parcial",
##        "dataSource": "Cluster0",
##        "projection": {
##        "_id": 1
##        }
##    })
##    headers = {
##        'Content-Type': 'application/json',
##        'Access-Control-Request-Headers': '*',
##        'api-key': 'Y49pKYsbRnhjIfcUDbMf3nwh0K4X6b6t0goJ9Dx6tGlS5lBmzYa8XbnFNCSLzW4l'
##    }
##    response = requests.request("POST", url, headers=headers, data=payload)
##    #print(response.text)
##
##    return response.text
    ##############################


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
