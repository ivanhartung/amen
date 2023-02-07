from flask import Flask, render_template, request, Response

app = Flask(__name__)


#@auth # lägg till auth decorator
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/profile")
def profile_page():
    return render_template("profile.html")

@app.route("/login")
def dummy_login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)