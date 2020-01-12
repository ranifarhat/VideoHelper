from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session

app = Flask(__name__)
app.secret_key = "8hf23782926hd4gdgdt72"


##### Code here ######

@app.route("/")
def home():
    return render_template("home.html")

#####################


if __name__ == '__main__':
    app.run(debug=True)