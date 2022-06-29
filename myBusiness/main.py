<<<<<<< HEAD
from flask import Flask,request, render_template, jsonify
import json
import requests
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import SubmitField, BooleanField, EmailField,StringField, PasswordField, validators
# from wtforms.validators import DataRequired,Email







#Form ----------------------------------------------
class SignInForm(FlaskForm):
    email = EmailField('Email Address')
    password = PasswordField('Password')
    submit = SubmitField('Log in')


class Resgistration(FlaskForm):
    lastName = StringField("Last Name")
    firstName = StringField("First Name")
    phoneNumber = StringField("Your Number")
    email = EmailField("Email Address")
    password = PasswordField('Password')
    submit = SubmitField("Sign me up ")




#Form ----------------------------------------------

#Key ----------------------------------------------
app = Flask(__name__)
app.config['SECRET_KEY'] = 'keyFormyDatabase'
#Key ----------------------------------------------


##CONNECT TO DB-----------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
##CONNECT TO DB-----------------



# userdatabase Table

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lastName = db.Column(db.String(250), nullable=False)
    firstName = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    phoneNumber= db.Column(db.String(250), nullable=False,unique=True)

    def __init__(self,lastName,firstName,email,password,phoneNumber):
        self.lastName = lastName
        self.firstName = firstName
        self.email = email
        self.password = password
        self.phoneNumber = phoneNumber

    def __repr__(self):
        return self.lastName


firstUser = {
    'lastName' : "Lam",
    'firstName': 'Van',
    'email': 'tienlam2001@gmail.com'
}

# for row in result:
#     print(row.password)

#
# lam = User('Lam', 'Van','tienlam2001@gmail.com','LamVan','3526617004')
# db.create_all()
#
# db.session.add(lam)
# db.session.commit()

@app.route("/")
def home():
    return render_template("home.html",title="Home Page")


@app.route("/main")
def mainPage(username):
    return render_template("mainPage.html",name=username,networth="$200,000",date="6/2/2022")


@app.route("/login")
def loginPage():
    formLogin = SignInForm()
    return render_template("login.html",title="login", form=formLogin )

@app.route("/signup")
def signUpPage():
    formSignup = Resgistration()
    return render_template('signup.html', title = "Sign Up | FinSolution", form=formSignup )

@app.route("/directMain",methods=["GET","POST"])
def verifyAccount():
    emailed = request.form['email']
    passworded = request.form['password']

    print()
    result = db.session.query(User).filter(User.email == emailed)

    print(result)
    # if emailed == firstUser['email']:
    #     return mainPage(firstUser['firstName'])
    # else:
    #     return loginPage()

    return loginPage()


@app.route("/directSigned", methods=["GET","POST"])
def accountSignedUp():
    return 0


@app.route("/balance")
def balanceSheet():
    with open('balance.json', 'r') as file:
        data = json.load(file)
        return jsonify(data)

@app.route("/asset")
def assetSheet():
    with open('asset.json', 'r') as file:
        data = json.load(file)
        return jsonify(data)

@app.route("/invest")
def investSheet():
    with open('invest.json', 'r') as file:
        data = json.load(file)
        return jsonify(data)

@app.route("/libability")
def libabilitySheet():
    with open('balance.json', 'r') as file:
        data = json.load(file)
        return jsonify(data)

@app.route("/netChange")
def incomeChange():
    with open('networth.json', 'r') as file:
        data = json.load(file)
        return jsonify(data)

@app.route("/paydebt")
def manageCard():
    return 0;

if __name__ == "__main__":
    app.run(debug=True,port='5000')
=======
from flask import Flask

>>>>>>> dcdedb30c13cdf04e5a18949728a1e2af61e2809
