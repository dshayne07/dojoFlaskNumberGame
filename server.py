from flask import Flask, render_template, session, redirect, request
import random

app = Flask(__name__)
app.secret_key="oiwajefoaiwnegwboughuao"

@app.route("/")
def index():
    session["result"] = ""
    if "rand" not in session:
        session["rand"] = random.randrange(0, 101)
    # if "guess" in session:
    #     if int(session["guess"]) == int(session["rand"]):
    #         session["result"] = "<p class='correct'>"+session["guess"]+" was the number!<br><a href='/'><button>Play again!</button></a></p>"
    #     elif int(session["guess"]) > int(session["rand"]):
    #         session["result"] = "<p class='wrong'>"+session["guess"]+" was too high!</p>"
    #     elif int(session["guess"]) < int(session["rand"]):
    #         session["result"] = "<p class='wrong'>"+session["guess"]+" was too low!</p>"

    return render_template("index.html")

@app.route("/guess", methods=["POST"])
def guess():
    session["guess"] = int(request.form["guess"])
    return redirect("/")

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

app.run(debug=True)