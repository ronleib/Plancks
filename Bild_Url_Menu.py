from datetime import time
from flask import request , json
import requests



def getMenu():
    url = "https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod=pickup"
    response = requests.request('GET' , url)
    time.sleep(5)
    jsonStr = json.dumps(response.text)
    jsonObj = json.loads(json.loads(jsonStr))
    return jsonObj

def getBate():
    order = request.data
    return json.loads(order)