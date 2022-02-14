from flask import Flask, render_template
import request
from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, EmailField,StringField, PasswordField, validators
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from wtforms import validators
from wtforms.validators import DataRequired,Email
import email_validator


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ThisisKey'


class RegForm(FlaskForm):
  email = EmailField('Email Address',validators=[DataRequired(), Email()])
  password = PasswordField('Password',validators=[DataRequired()])
  submit = SubmitField('Log in')

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = RegForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return  render_template('success.html')
        else :
            return  render_template('denied.html')
    return render_template('login.html', form = form)


if __name__ == '__main__':
    app.run(debug=True)