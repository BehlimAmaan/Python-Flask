from flask import Flask, render_template

app = Flask(__name__)
app.secret_key= "superkey"

@app.route("/")
def student():
    return render_template(
        "student_profile.html",
        name = "Amaan",
        is_topper = True,
        courses = ["CSE", "DATA SCIENCE", "AI & ML", "DevOps"]
    )

if __name__=="__main__":
    app.run(debug=True)