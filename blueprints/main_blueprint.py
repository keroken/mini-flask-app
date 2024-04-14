from flask import Blueprint, request, send_from_directory

main_views = Blueprint("main", __name__)

# Create routes on this blueprint instance


@main_views.get("/", strict_slashes=False)
def index():
    # Define application logic for homepage
    return "<h1>This is the Home Page</h1>"


@main_views.get("/profile/<string:username>", strict_slashes=False)
def profile(username):
    # Define application logic for profile page
    return f"<h1>Welcome {username}! This is your profile</h1>"


@main_views.get("/download/<str:filename>", strict_slashes=False)
def download(filename):
    # Using the send_from_directory function you can send a file
    # By providing the absolute path to the file
    # Note the /tmp/ is just for practice purpose.
    # You decide which directory you want to store your files at
    return send_from_directory(f"/tmp/Tutorial/{filename}")
