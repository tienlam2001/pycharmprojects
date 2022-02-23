from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from bs4 import BeautifulSoup
# import sqlite3

# db = sqlite3.connect("movieDatabase.db")
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movieDatabase.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)

# id
# title
# year
# description
# rating
# ranking
# review
# img_url
#Movie Object to Enter database
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    year = db.Column(db.Integer, nullable =False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=False)
    ranking = db.Column(db.Integer, unique=False, nullable=False)
    review = db.Column(db.Integer, unique=False, nullable=False)
    img_url = db.Column(db.String, unique=False, nullable=False)


    def __init__(self, title, year,description,rating,ranking,review,img_url):
        self.title = title
        self.year = year
        self.description = description
        self.rating = rating
        self.ranking = ranking
        self.review = review
        self.img_url = img_url

    def __repr__(self):
        return self.title


# db.create_all()

#Scrapping movie website and get data

def scraping():
    response = requests.get("https://www.bfi.org.uk/sight-and-sound/greatest-films-all-time")
    responseText = response.text
    soup = BeautifulSoup(responseText,"html.parser")
    articles = soup.find_all(name="h2",class_="sc-eCImPb MQmRY")
    # print(articles)

    return articles[0:10]

# new_movie = Movie(title="Phone Booth",year=2002,description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",rating=7.3,ranking=10,review="My favourite character was the caller.",img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg")

# db.session.add(new_movie)
# db.session.commit()










@app.route("/")
def home():
    myMovie = scraping()
    for movie in myMovie:
        print(movie.text)
    return render_template("index.html",movies = myMovie)

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/index")
def edit():
    return render_template("edit.html",  )

@app.route("/select")
def select():
    return render_template("select.html")


if __name__ == '__main__':
    app.run(debug=True)
