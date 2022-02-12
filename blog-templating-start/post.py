import requests
from flask import render_template

def getData('/data'):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    data = response.json()
    return render_template("post.html",)
