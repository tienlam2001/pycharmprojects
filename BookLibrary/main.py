from flask import Flask, render_template, request, redirect, url_for
import sqlite3

db = sqlite3.connect("books-collection.db")
cursor = db.cursor()
cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

app = Flask(__name__)

all_books = [
    {
        "title":"Harry Potter",
        "author":"J. K. Rowling",
        "rating":9
    },
    {
        "title":"Tale of Two Cities",
        "author":"Charles Dickens",
        "rating":7
    }
]


@app.route('/')
def home():
    return render_template("index.html", list= all_books)


@app.route("/add")
def add():
    pass


if __name__ == "__main__":
    app.run(debug=True)

