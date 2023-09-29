from flask import Flask , render_template

app = Flask (__name__)

@app.route("/")
def luiz():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("index-login.html")

@app.route("/homepageluiz")
def homepage_luiz():
    return render_template("index-home-luiz.html")

@app.route("/homepageamanda")
def homepagez_amanda():
    return render_template("index-home-amanda.html")

if __name__ == "__main__":
    app.run(debug=True)