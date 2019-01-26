from flask import Flask

app = Flask(__name__)



@app.route("CHAPTER1")

def chapter():
    
   return "welcome to CHAPTER1"
