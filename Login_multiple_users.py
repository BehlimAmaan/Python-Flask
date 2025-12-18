from flask import Flask, request, Response, redirect, url_for, render_template, session

app = Flask(__name__)
app.secret_key= "superkey"

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login",methods=["POST"])
def login():
    if request.method=="POST":
        username = request.form.get("username")
        password = request.form.get("password")

        valid_users = {
            "Amaan":"amaan@123",
            "Zaid":"zaid@123",
            "Zakwan":"zakwan@123"
        }
        session["valid_user"]=username
        if username in valid_users and password == valid_users[username]:
            return redirect(url_for("welcome"))
            
        else:
            return Response("Invalid Credentials",mimetype="text/plain")
    return render_template("login.html", name = username)

@app.route("/welcome")
def welcome():
    if "user" in session: 
       return render_template("welcome.html")
    return redirect(url_for("login"))

if __name__=="__main__":
    app.run(debug=True)