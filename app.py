from flask import Flask, jsonify
import json
import pymongo
import os


myclient = os.environ.get('MONGO_URI')
mydb = myclient["placementScraper"]
mycol = mydb["linkDB"]



app = Flask(__name__)





def updateLists():
    returnJson = []
    cursor = mycol.find({})
    for links in cursor:
        href = links['urLinkId']
        name = links['name']
        name = name.replace("\\u002e", "")
        href = href.replace("\\u002e", "")
        href = "https://amity.edu/placement/" + href
        returnJson.append({"title": name, "href": href})
    return returnJson



sampleDict = [
        {
            "title": "titl1", 
            "href": "google.com",
        },
        {
            "title": "titl2", 
            "href": "google.com",
        },
        {
            "title": "titl3", 
            "href": "google.com",
        },
        {
            "title": "titl4", 
            "href": "google.com",
        },
    ]

@app.route('/')
def home():
    returnJson = updateLists()
    json_object = json.dumps(returnJson, indent=4)
    return json_object
    

if __name__ == '__main__':
    app.run(debug=True)