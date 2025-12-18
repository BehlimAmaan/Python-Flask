from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def Home():
    return 'This is a Home Page'

@app.route("/about")
def about():
    return 'This is a About page'

@app.route('/about/contact')
def contact():
    return 'This is a Contact Page'

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        return 'You Send a Data'
    else:
        return 'You are Just Viewing'
    


if __name__=="__main__":
    app.run(debug=True)