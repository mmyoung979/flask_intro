from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    context = {"name": "Boruto", "age": 14, "type": "lightning", "shinobi": True}
    return render_template("home.html", context=context)
