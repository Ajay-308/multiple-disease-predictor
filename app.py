from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import pickle
import numpy as np


app = Flask(__name__)

app.secret_key = "2101MM"
app.config["MYSQL_HOST"] = "db4free.net"  # Update this with the actual host
app.config["MYSQL_USER"] = "rock123"
app.config["MYSQL_PASSWORD"] = "rock1234"
app.config["MYSQL_DB"] = "rock123"

mysql = MySQL(app)

# instantiate object

# loading the different saved model for different disease
diabetes_predict = pickle.load(open("diabetes.pkl", "rb"))
heart_predict = pickle.load(open("heart.pkl", "rb"))
parkinsons_predict = pickle.load(open("parkinsons.pkl", "rb"))


@app.route("/")  # instancing one page (homepage)
def main():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    msg = ""
    if (
        request.method == "POST"
        and "username" in request.form
        and "password" in request.form
    ):
        username = request.form["username"]
        password = request.form["password"]
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            "SELECT * FROM account1 WHERE username = %s AND password = %s",
            (
                username,
                password,
            ),
        )
        account = cursor.fetchone()
        if account:
            session["loggedin"] = True

            msg = "Logged in successfully !"

            return render_template("layout.html", msg=msg)
        else:
            msg = "Incorrect username / password !"
    return render_template("login.html", msg=msg)


@app.route("/logout")
def logout():
    session.pop("loggedin", None)
    session.pop("id", None)
    session.pop("username", None)
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    msg = ""
    if (
        request.method == "POST"
        and "username" in request.form
        and "password" in request.form
        and "email" in request.form
    ):
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM account1 WHERE username = %s", (username,))
        account = cursor.fetchone()
        if account:
            msg = "Account already exists !"
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            msg = "Invalid email address !"
        elif not re.match(r"[A-Za-z0-9]+", username):
            msg = "Username must contain only characters and numbers !"
        elif not username or not password or not email:
            msg = "Please fill out the form !"
        else:
            cursor.execute(
                "INSERT INTO account1 VALUES (NULL, % s, % s, % s)",
                (
                    username,
                    password,
                    email,
                ),
            )
            mysql.connection.commit()
            msg = "You have successfully registered !"
    elif request.method == "POST":
        msg = "Please fill out the form !"
    return render_template("register.html", msg=msg)


def home():
    return render_template("home.html")


# ^^ open home.html, then see that it extends layout.
# render home page.


@app.route("/diabetes")  # instancing child page
def diabetes():
    return render_template("diabetes.html")


@app.route("/parkinsons/")  # instancing child page
def parkinsons():
    return render_template("parkinsons.html")


@app.route("/heartdisease/")  # instancing child page
def heartdisease():
    return render_template("heartdisease.html")


@app.route("/predictdiabetes/", methods=["POST"])
def predictdiabetes():  # function to predict diabetes
    int_features = [x for x in request.form.values()]
    processed_feature_diabetes = [np.array(int_features, dtype=float)]
    prediction = diabetes_predict.predict(processed_feature_diabetes)
    if prediction[0] == 1:
        display_text = "This person has Diabetes"

    else:
        display_text = "This person doesn't have Diabetes"
    return render_template(
        "diabetesprecaution.html", output_text="Result: {}".format(display_text)
    )


@app.route("/predictparkinson/", methods=["POST"])
def predictparkinsons():  # function to predict parkinsons disease
    int_features = [x for x in request.form.values()]
    processed_feature_parkinsons = [np.array(int_features, dtype=float)]
    prediction = parkinsons_predict.predict(processed_feature_parkinsons)
    if prediction[0] == 1:
        display_text = "This person has Parkinson's"
    else:
        display_text = "This person doesn't have Parkinson's"
    return render_template(
        "parikson_precaution.html", output_text="Result: {}".format(display_text)
    )


@app.route("/predictheartdisease/", methods=["POST"])
def predictheartdisease():  # function to predict heart disease
    int_features = [x for x in request.form.values()]
    processed_feature_heart = [np.array(int_features, dtype=float)]
    prediction = heart_predict.predict(processed_feature_heart)
    if prediction[0] == 1:
        display_text = "This person has Heart Disease"
    else:
        display_text = "This person doesn't have Heart Disease"
    return render_template(
        "heartPrecautions.html", output_text="Result: {}".format(display_text)
    )


if __name__ == "__main__":
    app.run(debug=True)
