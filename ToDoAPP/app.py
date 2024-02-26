from flask import Flask ,render_template, request, redirect, url_for

app = Flask(__name__)

toDos = []

@app.route("/")
def list_toDo():
    return render_template("list_toDo.html",toDos = toDos)

@app.route("/add", methods = ["POST"])
def add_toDo():
    toDo = request.form["toDo"]
    toDos.append(toDo)
    return redirect(url_for("list_toDo"))






app.run(debug = True)
