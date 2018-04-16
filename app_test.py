from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcom Raja!!"

app.run(port=5000)