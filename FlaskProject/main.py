from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def helloworld():
    return render_template('index.html')

# @app.route("/bye")
# def bye():
#     return "Buy"
#
# @app.route("/username/<name>")
# def thisPrint(name):
#     return f"Hello {name}"
#
if __name__ == '__main__':
    app.run(debug=True)