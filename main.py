from flask import Flask
app = Flask(__name__)

@app.route("/api")
def first():
    return "Hello, world"
