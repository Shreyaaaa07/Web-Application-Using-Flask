from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
app.run(debug=True)

@app.route('/services')
def services():
    return render_template('services.html')
app.run(debug=True)


@app.route('/CONTACT')
def contact():
    return render_template('contact.html')
app.run(debug=True)


@app.route('/about')
def about():
    return render_template('about.html')
app.run(debug=True)