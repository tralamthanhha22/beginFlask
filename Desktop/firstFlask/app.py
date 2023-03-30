from flask import Flask, redirect, url_for,render_template,request
app=Flask(__name__)
@app.route('/')
def home():
    return render_template("home.html")
#get request
@app.route('/user/<name>')
def name(name):
    return f"<h1> {name} </h1>"
#post request 
@app.route('/login',methods=["POST","GET"])
def login():
    if request.method=="POST":
        user_name=request.form["user"]# pick from user type on web, set value name="" in html
        if user_name:
            return redirect(url_for("name",name=user_name)) # set value for parameter in def name(name)
    return render_template("login.html")
if __name__ =="__main__":
    #app.run(debug=True)
    app.run()