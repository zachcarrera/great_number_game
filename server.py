import random
from flask import Flask, render_template, session, redirect, request, flash

app = Flask(__name__)
app.secret_key = "password"

wrong_response = "<div class='mx-auto my-3 w-80 p-3 flex justify-center bg-red-500 text-slate-200 rounded-lg'><p>Too {}!</p></div>"


@app.route("/")
def index():
    if "answer" not in session:
        session["answer"] = random.randint(1, 100)

    return render_template("index.html")


@app.route("/guess", methods=["POST"])
def process_guess():
    if request.form["number"] == "":
        flash("Please enter a number")
        return redirect("/")

    guess = int(request.form["number"])
    if guess > session["answer"]:
        print("Guess is too high")
        session["response"] = wrong_response.format("high")

    elif guess < session["answer"]:
        print("Guess is too low")
        session["response"] = wrong_response.format("low")

    else:
        print("Guessed the number!")
        session["response"] = f"<div class='mx-auto my-3 w-80 flex flex-col items-center p-3 bg-green-500 text-slate-200 rounded-lg gap-4'><p>{guess} was the number!</p><form action='/start_game' method='post'><input type='submit' value='Play again!' class='text-white bg-blue-700 hover:bg-blue-800 rounded-lg px-5 py-2.5'></form></div>"

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
