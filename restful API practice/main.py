from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pandas
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random", methods=["GET"])
def randomFunction():
    coffee = db.session.query(Cafe).all()    
    random_cafe = random.choice(coffee)
    return jsonify(cafe={
        "id": random_cafe.id,
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "seats": random_cafe.seats,
        "location":random_cafe.location,
        "has_wifi": random_cafe.has_wifi,
        "can_take_calls": random_cafe.can_take_calls,
    })

array = []
coffee = db.session.query(Cafe).all()
for i in range(len(coffee)):
    cafe = {
        "id": coffee[i].id,
        "name": coffee[i].name,
        "map_url": coffee[i].map_url,
        "img_url": coffee[i].img_url,
        "seats": coffee[i].seats,
        "has_wifi": coffee[i].has_wifi,
        "location": coffee[i].location,
        "can_take_calls": coffee[i].can_take_calls,
    }
    array.append(cafe)

@app.route("/all", methods=["GET"])
def getAll():
    global array
    return jsonify(array)


@app.route("/search", methods=["GET"])
def getSearch():
    global array
    query_location = request.args.get("loc")
    print(query_location)
    for i in array:
        print(i['location'])
        if i["location"] == query_location:
            return jsonify(i)

    return jsonify(error="error")


if __name__ == '__main__':
    app.run(debug=True,port=5000)
