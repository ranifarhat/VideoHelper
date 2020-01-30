from flask import Flask, request, redirect, url_for, render_template, flash
from flask import session as login_session

from database import add_user, query_all

app = Flask(__name__)
app.secret_key = "8hf23782926hd4gdgdt72"
# app.config('SECRET_KEY') = 'sdfgyugw76e231yhih'



##### Code here ######

@app.route("/", methods=["GET", "POST"])
def home():
	if request.method == "GET":
		return render_template("home.html")
	else:
		search_res = request.form["srch"]

		if search_res == "" or search_res == " ":
			flash("Can't enter with search empty")
			return render_template("home.html")
		else:

			yt_srch_link = "https://www.youtube.com/results?search_query="

			final_res = yt_srch_link + search_res 
			return render_template("redirect_p.html", fin=final_res)


@app.route("/redirect")
def redirect():
	return render_template("redirect_p.html")

@app.route("/community")
def community():
	return render_template("community.html")

@app.route("/create-group")
def group_creation():
	return render_template("create_group.html")

@app.route("/signup-in", methods=["GET", "POST"])
def signupin():
	if request.method == "GET":
		return render_template("signupin.html")
	else:
		uname = request.form["name"]
		mail = request.form["email"]
		passw = request.form["psw"]
		passw_re = request.form["psw-rep"]

		for prod in query_all():
			if(mail == prod.email):
				print("hhh")
				flash("Email already used, please sign in or use different email")
				return render_template("signupin.html")


		if mail.find("@") == -1 or mail.find(".") == -1:
			flash("Invalid email")
			return render_template("signupin.html")
		elif passw != passw_re:
			flash("Password do not match")
			return render_template("signupin.html")
		elif len(passw) < 8 and passw[0] != " ":
			flash("Password has to be at least 8 characters and can't start with a space")
			return render_template("signupin.html")
		else:
			add_user(mail, uname, passw)
			return render_template("home.html", n=uname)

#####################


if __name__ == '__main__':
    app.run(debug=True)