from flask import Flask, render_template, redirect

app = Flask(__name__);
head = "Measure Once Cut Thrice"
foot = "quality_assurance"

@app.route("/")
def first():
    return redirect("/login");

@app.route("/login")
def home():
    return render_template("login.html", header=head,
                            footer=foot);

@app.route("/signup")
def signup():
    return render_template("signup.html", header=head,
                            footer=foot);

@app.route("/home")
def homepage():
    return render_template("home.html", currentUser="gmao00");

if __name__ == "__main__":
    app.debug = True
    app.run()
