from flask import Flask
app = Flask(__name__)

@app.route("CHAPTER2")
def chapter():
    return "welcome to CHAPTER2"
