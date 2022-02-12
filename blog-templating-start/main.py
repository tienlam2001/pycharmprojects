from flask import Flask, render_template
import requests
import numpy as np



#https://api.npoint.io/c790b4d5cab58020d391
app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    datas = response.json()
    return render_template("index.html", blog=datas)

@app.route("/blog/<num>")
def openBlog(num):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    datas = response.json()
    my_array = np.array(datas)
    return render_template("post.html", title = my_array[int(num) - 1]["title"], body = my_array[int(num)- 1]["body"])

if __name__ == "__main__":
    app.run(debug=True)
