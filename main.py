from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

## POST Method
@app.route("/submit_data", methods=["POST"])
def submit_data():
    name = request.args.get("name")
    age = request.args.get("age")
    email = request.args.get("email")
    password = request.args.get("password")
    return render_template("submit_data.html", name=name, age=age, email=email, password=password)

## GET Method
"""
@app.route("/submit_data", methods=["GET"])
def submit_data():
    name = request.args.get("name")
    age = request.args.get("age")
    email = request.args.get("email")
    password = request.args.get("password")
    return render_template("submit_data.html", name=name, age=age, email=email, password=password)
"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3333)

