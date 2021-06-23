from bs4 import BeautifulSoup
import requests
import time, json
import pymongo
import unixTimeStamp
import os


configKey = os.environ.get('MONGO_KEY')
myclient = pymongo.MongoClient(configKey)
mydb = myclient["placementScraper"]
mycol = mydb["linkDB"]




urlLinkpre = "https://amity\\u002eedu/placement/"




def updateLists():
    # global currentHeaders, currentLinks
    
    currentLinks = []
    currentHeaders = []
    cursor = mycol.find({})
    for links in cursor:
        currentLinks.append(links['urLinkId'])
        currentHeaders.append(links['name'])
    return [currentHeaders, currentLinks]


# Main Scraper
def scraper(url):
    resp = updateLists()
    currentHeaders = resp[0]
    currentLinks = resp[1]
    print("\n old list is ", currentHeaders, end="\n")
    n1 = "name"
    urlID = "urLinkId"
    urLinkM = "urLinkMain"
    currentTime = "currTime"
    checkLast = unixTimeStamp.checkAndUpdateTime()
    if checkLast == 0:
        print("Request not being made")
        return json.dumps({"name": {"headerlist": currentHeaders}, "links": {"linkslist": currentLinks}, "newLinks": "No", "requestMade": "No"})
    else:  
        print("Request being made and the new list is : - ", end="\n")    
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        divRequired = soup.find('ul', class_ = 'notices')
        lists = divRequired.findAll('li')
        for li in lists:
            # print(li)
            name = str(li.a.strong.text)
            print(name)
            urLinkId = str(li.a["href"])
            urLinkId = urLinkId.replace(".", "\\u002e")
            urLinkMain = urlLinkpre + urLinkId
            currTime = str(int(time.time()))
            flag = 0
            if name not in currentHeaders:
                name = name.replace('.', "\\u002e")
                print("New link found")
                uploadLinks = {n1: name, urlID: urLinkId, urLinkM: urLinkMain, currentTime: currTime}
                db_upload = mycol.insert_one(uploadLinks)
                # print(db_upload)
                flag = 1
            else:
                continue
        # updateLists()
        if flag == 1:  
            return json.dumps({"name": {"headerlist": currentHeaders}, "links": {"linkslist": currentLinks}, "newLinks": "Yes", "requestMade": "Yes"})
        else:
            # print(json.dumps({"name": {"headerlist": currentHeaders}, "links": {"linkslist": currentLinks}, "newLinks": "No", "requestMade": "Yes"}))
            return json.dumps({"name": {"headerlist": currentHeaders}, "links": {"linkslist": currentLinks}, "newLinks": "No", "requestMade": "Yes"})

