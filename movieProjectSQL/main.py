from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movieDatabase.db"
db = SQLAlchemy(app)
Bootstrap(app)


#Scrapping movie website and get data

def scraping():
    response = requests.get("https://www.bfi.org.uk/sight-and-sound/greatest-films-all-time")
    responseText = response.text
    soup = BeautifulSoup(responseText,"html.parser")
    articles = soup.find_all(name="h2",class_="sc-eCImPb MQmRY")
    # print(articles)

    return articles[0:10]








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
