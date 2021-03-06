from flask import Flask, render_template, url_for





app = Flask(__name__)


@app.route("/")
def index():
    return render_template("root_layout.html")

@app.route("/auth/login")
def auth_login():
    return render_template("login.html")    

@app.route("/auth/signup")
def auth_signup():
    return render_template("signup.html")

@app.route("/contact")   
def contact():
    return render_template("contact.html") 

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/forum")
def forum():
    return render_template("forum.html")   

@app.route("/events")  
def events():
    return render_template("events.html")   





