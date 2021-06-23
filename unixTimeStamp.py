
# this function is needed because my scraper has to work only twice during a day and each time a request is made it checks
# whether or not half a day has passed since last scrape

import time
import pymongo
from pymongo import cursor
import os

configKey = os.environ.get('MONGO_KEY')
myclient = pymongo.MongoClient(configKey)
mydb = myclient["placementScraper"]
mycol = mydb["unixTimeStamp"]

# cursor = mycol.find({})

currTime = int(time.time())



# this function used for the first time to make a record. It has no use now.
def insertTime():
    m = {"currTime": currTime}
    try:
        uploadStatus = mycol.insert_one(m)
        print(uploadStatus)
        return 1
    except:
        return 0


# this function checks the time and returns the status accordingly. If more than half a day, updates in database too
def checkAndUpdateTime():
    cursor = mycol.find({})
    id = 0
    lastTime = 0
    for t in cursor:
        lastTime = t['currTime']
        print(lastTime)
        id = t['_id']
        
    # if currTime - lastTime >= 100:
    if currTime - lastTime >= 43200:    
        try:
            q1 = {'_id': id}
            new_val = {"$set": {"currTime": currTime}}
            mycol.update_one(q1, new_val)
            print("update successful")
        except:
            print("Error Occured")
            return "Error Occured"
        return 1
    else:
        #  since not half a day passed
        return 0

# if __name__ == '__main__':
#     checkAndUpdateTime()