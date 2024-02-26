from flask import Flask ,render_template

app = Flask(__name__)

@app.route("/")
def page1():
    return "Hello, World!"

@app.route("/a")
def page2():
    return render_template("page1.html")



app.run(debug = True)
