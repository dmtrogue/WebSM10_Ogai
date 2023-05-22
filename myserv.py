from flask import Flask, render_template,request
from json import dumps as jsonstring

app = Flask(__name__)

class Street(object):
    def __init__(self, name, houses, house_area, street_long):
        self.name = name
        self.houses = houses
        self.house_area = house_area
        self.street_long = street_long

    def __str__(self, name, count_house, house_area, street_long):
        return("Название улицы: ",name,
                " Количество домов:",count_house,
                " Площадь домов в М^2:",house_area,
                " Длина улицы в КМ:", street_long)

class House(object):
    def __init__(self, number, count_flats, count_floors,image):
        self.number = number
        self.count_flats = count_flats
        self.count_floors = count_floors
        self.image = image

house_10 = House(10,200,25,"house_10.jpg")
house_9 = House(9,100,5,"house_9.jpg")
house_17 = House(17,180,10,"house_17.jpg")

houses = [house_10,house_17,house_9]

street_pushkina = Street("Пушкина",houses, 10000,20)

@app.route("/")
def hello_world():
    return render_template('lab4.html',street = street_pushkina)

@app.route("/new_house")
def adding():
    number = request.args.get('number')
    count_flats = request.args.get('count_flats')
    count_floors = request.args.get('count_floors')
    new_house = House(number,count_flats,count_floors,"new_house.jpg")
    street_pushkina.houses.append(new_house)
    return "Добавил"

@app.route("/delete")
def deleting():
    number = request.args.get('number')
    c = 0
    for h in street_pushkina.houses:
        if h.number == number:
            del street_pushkina.houses[c]
            return "Удалил" + h.number
        else:
            c = c + 1
    return "Не нашёл такой дом"