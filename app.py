from flask import Flask, jsonify
import json

app = Flask(__name__)


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
    json_object = json.dumps(sampleDict, indent=4)
    return json_object
    

if __name__ == '__main__':
    app.run(debug=True)