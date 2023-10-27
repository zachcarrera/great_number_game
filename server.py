import random
from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = "password"


@app.route("/")
def index():

    if "answer" not in session:
        session["answer"] = random.randint(1, 100)

    return render_template("index.html")


@app.route("/guess", methods=["POST"])
def process_guess():
    guess = int(request.form["number"])
    if guess > session["answer"]:
        print("Guess is too high")
        session["response"] = "<div class='row d-flex justify-content-center my-3'><div class='col-3 bg-danger text-light p-3 d-flex justify-content-center'><p>Too high!</p></div></div>"

    elif guess < session["answer"]:
        print("Guess is too low")
        session["response"] = "<div class='row d-flex justify-content-center my-3'><div class='col-3 bg-danger text-light p-3 d-flex justify-content-center'><p>Too low!</p></div></div>"

    else:
        print("Guessed the number!")
        session["response"] = f"<div class='row d-flex justify-content-center my-3'><div class='col-3 bg-success text-light p-3 d-flex flex-column align-items-center'><p>{guess} was the number!</p><form action='/start_game' method='post'><input type='submit' value='Play again!' class='btn btn-primary'></form></div></div>"

    return redirect("/")


# stacked routes to restart the game
@app.route("/reset")
@app.route("/start_game", methods=["POST"])
def restart():
    session.clear()
    session["answer"] = random.randint(1, 100)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
