from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)



app.config['SECRET_KEY'] = "rupees"
app.config['SQLALCHEMY_DATABASE-URI'] ='sqlite:///data.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.column(db.Integer)

@app.route('/',methods=['GET','POST'])
def auth():
    if request.method=="POST":
        name = request.form[ 'name' ]
        email = request.form[ 'email' ]
        pass1 = request.form[ 'password' ]
        pass2 = request.form[ 're_password' ]

        if pass1==pass2:
            flash('your account register successfully!')
            print("success")
        else:
            flash('password is not match')

            print("password is not match")

    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)