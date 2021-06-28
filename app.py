from flask import Flask, jsonify
import json
import pymongo
import os
import scraper
import unixTimeStamp
import time

uri = os.environ.get('MONGO_URI')
myclient = pymongo.MongoClient(uri)
mydb = myclient["placementScraper"]
mycol = mydb["linkDB"]



app = Flask(__name__)


url = "https://amity.edu/placement/upcoming-recruitment.asp"


# def updateLists():
#     returnJson = []
#     cursor = mycol.find({})
#     for links in cursor:
#         href = links['urLinkId']
#         name = links['name']
#         name = name.replace("\\u002e", ".")
#         href = href.replace("\\u002e", ".")
#         href = "https://amity.edu/placement/" + href
#         returnJson.append({"title": name, "href": href})
#     return returnJson

@app.route('/')
def home():
    return "App switched off"

# @app.route('/')
# def home():
#     timeCheck = unixTimeStamp.checkAndUpdateTime() 
#     if timeCheck == 0:
#         returnJson = updateLists()
#         json_object = json.dumps(returnJson, indent=4)
#         return json_object
#     else:
#         newScraped = scraper.scraper(url)
#         returnJson = updateLists()
#         json_object = json.dumps(returnJson, indent=4)
#         return json_object
#     return [{"title": "Programming error"}]

    

if __name__ == '__main__':
    app.run(debug=True)
