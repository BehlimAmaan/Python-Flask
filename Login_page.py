from flask import Flask, Response, request, redirect, session, url_for, render_template

app = Flask(__name__)
app.secret_key="supersecret"

@app.route("/", methods=["GET","POST"])
def login():
    if request.method== "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if username=="admin" and password=="123":
            session["user"]= username
            return redirect(url_for("welcome"))
        else:
            return Response('Invalid Credentials ', mimetype="text/plain")
             
    return render_template("login.html")

@app.route("/welcome")
def welcome():
    if "user" in session:
        return render_template("welcome.html")
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("login"))
    
    
if __name__=="__main__":
    app.run(debug=True)

 
            