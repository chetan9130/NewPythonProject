from flask import  Flask,render_template
app = Flask(__name__)
@app.route("/")
def home():
    l1=[1,2,3,4]
    return render_template("index.html",data=l1)
@app.route("/user/<id>")
def user(id):
    return render_template("new.html",id=id)

if __name__ == "__main__":

    app.run(debug=True)