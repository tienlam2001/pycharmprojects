from flask import Flask, jsonify,render_template, request, url_for, redirect, flash, send_from_directory
import requests
import json

app = Flask(__name__)

@app.route("/books")
def api():
    with open('data.json', 'r') as file:
        data = json.load(file)
        return jsonify(data)

@app.route("/")
def main():
    with open('data.json', 'r') as file:
        data = json.load(file)
        key =list(data.keys())
        length = len(data.keys())
        print(length)
        print(key)
        return render_template("home.html", datas=data, keys=key,longArray=length)

@app.route("/book/<name>")
def home(name):
    with open('data.json', 'r') as file:
        data = json.load(file)
        return render_template("index.html",datas=data[name]['Idea'],line=name,image=data[name]['url'])



@app.route('/handle/<de>',methods=['get','post'])
def handleInput(de):
    input = request.form['idea']
    with open('data.json', 'r') as file:
        data = json.load(file)
        updateFile = data[de]['Idea']
        with open('data.json', 'w') as file2:
            updateFile.append(input)
            data[de]['Idea'] = updateFile
            json.dump(data, file2, indent=4)



    return home(de)

if __name__ == "__main__":
    app.run(debug=True,port=5000)