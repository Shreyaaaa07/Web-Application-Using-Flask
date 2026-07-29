from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks = {
        "john": 45,
        "Atharva":99,
        "Marks": 45,
        "jeff": 67,
        "Alexa": 90,
        "lily": 100
    }
    return render_template("index.html", marks = marks)

app.run(debug=True)