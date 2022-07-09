from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB.
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register',methods=['GET','POST'])
def register():
    try:
        nameUser = request.form['name']
        emailUser = request.form['email']
        passwordUser = request.form['password']
        print(nameUser)
        newUser = User(email=emailUser,password=passwordUser,name=nameUser)
        db.session.add(newUser)
        db.session.commit()
    except:
        print("Error")


    return render_template("register.html")


@app.route('/login',methods=['GET','POST'])
def login():
    try:
        findUser = User.query.filter_by(email=request.form['email']).first()
        if findUser == None:
            raise ValueError("Hmm")
        else:
            # if findUser.password == request.form['password']:
            return secrets(findUser.name)
            # else:
            #     pass
    except:
        print("error")

    return render_template("login.html")


@app.route('/secrets')
def secrets(name):
    return render_template("secrets.html",title=name)


@app.route('/logout')
def logout():
    pass


@app.route('/download')
def download():
    return send_from_directory('')

if __name__ == "__main__":
    app.run(debug=True,port=3000)
