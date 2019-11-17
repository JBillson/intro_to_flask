from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = "secretkey"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["_name"]
        age = request.form["_age"]
        session["user"] = user 
        session["age"] = age
        flash("Login Successful!", "info")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already logged in!", "info")
            return redirect(url_for("user"))

        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        age = session["age"]
        return render_template("user.html", user=user, age=age)
    else:
        flash("Sorry, you are not logged in, please login first", "info")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    flash(f"User has been logged out!", "info")
    session.pop("user", None)
    session.pop("age", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
 
