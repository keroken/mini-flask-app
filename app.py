from flask import Flask

# create instance of the flask app
app = Flask(__name__)

# create a route on your app


@app.route("/", strict_slashes=False, methods=["GET"])
def index():
    return "<h1>this is the home page</h1>"
