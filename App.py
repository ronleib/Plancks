import time
from flask import Flask , json

from Bild_Url_Menu import getMenu ,getBate
from price import price

from Arrange_Data import List_Data


app = Flask(__name__)

data = getMenu()

List_Pizzas = List_Data(data,"Pizzas")
List_Drinks = List_Data(data,"Drinks")
List_Desserts = List_Data(data,"Desserts")


@app.route('/')
@app.route('/drinks', methods=['GET'])
def getAlldrinks():
    return List_Drinks


@app.route('/drink/<id>', methods=['GET'])
def getDrink(id):
    return List_Drinks[id]

@app.route('/pizzas', methods=['GET'])
def getAllPizzas():
    return List_Pizzas


@app.route('/pizza/<id>', methods=['GET'])
def getPizza(id):
    return List_Pizzas[id]

@app.route('/desserts', methods=['GET'])
def getAllDesserts():
    return List_Desserts


@app.route('/dessert/<id>', methods=['GET'])
def getDessert(id):
    return List_Desserts[id]

#@app.route('/order', methods=['POST'])
#def getOrder():
    Bate = getBate()
    #price1 = price(Bate,List_Desserts,List_Drinks,List_Pizzas)
    #t=0;
    #for x in data['drinks']:
    #price1 = List_Drinks[data['drinks'][t]]
    #return price1


if __name__ == "__main__":
    app.run(debug=True)