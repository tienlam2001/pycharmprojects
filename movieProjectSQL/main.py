from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from bs4 import BeautifulSoup
#import sqlite3

#db = sqlite3.connect("movieDatabase2.db")
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movieDatabase2.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)


#Movie Object to Enter database
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    year = db.Column(db.Integer, nullable =False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=False)
    ranking = db.Column(db.Integer, unique=False, nullable=False)
    review = db.Column(db.String, unique=False, nullable=False)
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

class EditForm(FlaskForm):
    rating = StringField('Rating', validators=[DataRequired()])
    review = StringField('Review', validators=[DataRequired()])
    submit = SubmitField("Update")

class AddForm(FlaskForm):
    title = StringField('Name', validators=[DataRequired()])
    year = StringField('Year', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    rating = StringField('Rating', validators=[DataRequired()])
    ranking = StringField('Ranking', validators=[DataRequired()])
    review = StringField('Review', validators=[DataRequired()])
    img_url = StringField('Image', validators=[DataRequired()])
    submit = SubmitField("Add")



# db.create_all()

#Scrapping movie website and get data

def scraping():
    response = requests.get("https://www.bfi.org.uk/sight-and-sound/greatest-films-all-time")
    responseText = response.text
    soup = BeautifulSoup(responseText,"html.parser")
    articles = soup.find_all(name="h2",class_="sc-eCImPb MQmRY")
    # print(articles)
    return articles[0:10]

#



# Get data from database

def fetchData():
    allMovies = db.session.query(Movie).all()
    return allMovies

@app.route("/")
def home():
    myMovie = fetchData()
    return render_template("index.html",movies=myMovie)

@app.route("/add",methods=["GET","POST"])
def update():
    addForm = AddForm()
    if addForm.title.data != None:
        new_movie = Movie(title="Phone Booth",year=2002,description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",rating=7.3,ranking=10,review="My favourite character was the caller.",img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg")
    return render_template("add.html", form=addForm)




@app.route("/edit/<name>",methods=["GET","POST"])
def edit(name):
    form2 = EditForm()
    print(form2.rating.data)
    if form2.rating.data ==None and form2.review.data == None:
        return render_template("edit.html", form=form2, movieName=name)
    else:
        movietoupdate = Movie.query.filter_by(title=name).first()
        movietoupdate.rating = float(form2.rating.data)
        movietoupdate.review = form2.review.data
        db.session.commit()
        return home()

# @app.route("/successedit")
# def success():
#     myMovie = fetchData()
#     formdata = reques
#     return render_template("index.html", movies=myMovie)


@app.route("/select")
def select():
    return render_template("select.html")


if __name__ == '__main__':
    app.run(debug=True)
