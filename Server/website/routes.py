from website import app
from flask import render_template
from flask import request


@app.route("/")
def create_app():
    # reminder make a template folder for the html so it can go find the html in the template folder
    # put justin html file here debug.html is a debugging file
    return render_template("debug.html", debug=True)


# needs justin html to do the post
app.route("/", methods=["POST", "GET"])


def add_customer():
    if request.method == "POST":
        pass
        username = request.form.get()  # store the form name
        comment = request.form.get()  # store the form name
        upload_picture = request.form.get()  # store the form name
        ratings = request.form.get()  # store the form name


db."""name of collection""".insertOne():
{
    "username": username,
    "comment": comment,
    "upload_picture": upload_picture,  # might need to make this true or false
    "ratings": ratings

}
