from flask import Flask, render_template, request,redirect,url_for

app = Flask(__name__)
import smtplib







@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def aboutPage():
    return render_template("about.html")


#
@app.route('/contact')
def contactForm():
    return render_template('contact.html')

@app.route('/login', methods=["POST"])
def receive_data():
    name=request.form["username"]
    email = request.form["email"]
    myemail = "vde821149@gmail.com"
    phoneNumber = request.form['phone']
    message = request.form['message']
    connection = smtplib.SMTP("smtp.gmail.com")

    connection.starttls()
    connection.login(user=myemail, password="deVan123")
    connection.sendmail(from_addr=myemail, to_addrs="nghia.van0910@gmail.com",
                        msg=f'Subject:Quote For The Day \n\n name : {name} \n email : {email} \n Phone Number: {phoneNumber} \n message: {message} ')
    connection.close()
    return redirect(url_for('contactForm',name = name))

if __name__ == '__main__':
    app.run(debug=True)