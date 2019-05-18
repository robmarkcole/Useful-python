# run with $ flask run

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Robin!"

if __name__ == "__main__":
    app.run()
