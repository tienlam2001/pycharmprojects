from flask import Flask, render_template
import json

app =  Flask(__name__)

images = ["html.png","csslogo.png","reactjs.png","javascript.png","phplogo.png","pythonIcon.png","javaIcon.png"]
#
#
#
# json_object = json.dumps(textData, indent=4)
#
# # Writing to sample.json
# with open("data.json", "w") as outfile:
#     outfile.write(json_object)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def renderAbout():
    return render_template("about.html")

@app.route("/skill")
def renderSkill():
    return render_template("skillPage.html", images=images)

if __name__ == '__main__':
    app.run(debug=True)