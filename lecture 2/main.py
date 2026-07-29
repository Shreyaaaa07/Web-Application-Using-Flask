from flask import Flask, request, render_template

app = Flask(__name__)
@app.router("/", methods=["GET", "POST"])
def hello_world():
    if(request.method):
        #handle the form 
        with open("file.text", "w") as f:
                  f.write(f"The name is {request.form['name']}, the email is {request.form['email']}, ")
                  
        return render_template("contact.html")

    else:
        return render_template("contact.html")

    return render_template("contact.html")
app.run(debug=True)