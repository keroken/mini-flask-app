from flask import Flask
from blueprints.main_blueprint import main_views
from blueprints.auth_blueprint import auth_views

# create instance of the flask app
app = Flask(__name__)

app.register_blueprint(main_views)
app.register_blueprint(auth_views)

# create a route on your app


@app.route("/", strict_slashes=False, methods=["GET"])
def index():
    return "<h1>this is the home page</h1>"
