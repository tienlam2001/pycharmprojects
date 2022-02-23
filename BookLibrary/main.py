from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy

# db = sqlite3.connect("new-books-collection.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT OR IGNORE INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()




app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, unique=False, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=False)

    def __init__(self, title, author, rating):
        self.title = title
        self.author = author
        self.rating = rating

    def __repr__(self):
        return self.title

## Trying to commit the database with information data
# db.create_all()
# book = Book('Tale of Two Cities', 'Charles Dicken', 7)
# db.session.add(book)
# db.session.commit()




# all_books = [
#     {
#         "title":"Harry Potter",
#         "author":"J. K. Rowling",
#         "rating":9
#     },
#     {
#         "title":"Tale of Two Cities",
#         "author":"Charles Dickens",
#         "rating":7
#     }
# ]


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", list= all_books)


@app.route("/",methods=['GET', 'POST'])
def add():
    global db
    titleBook = request.form['title']
    authorBook = request.form['author']
    ratingBook = request.form['rating']
    if titleBook != "":
        book = Book(titleBook, authorBook, float(ratingBook))
        db.session.add(book)
        db.session.commit()

    all_books = db.session.query(Book).all()
    return render_template("index.html", list=all_books)


@app.route('/add')
def renderAdd():
    return render_template("add.html",value ="None")

@app.route('/edit/<data>/<author>/<rating>')
def edit(data,author,rating):
    return render_template("add.html",value = data,valueAuthor=author,valueRating = rating)



if __name__ == "__main__":
    app.run(debug=True)

