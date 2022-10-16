import random
from http import HTTPStatus
from datetime import datetime
import os
from flask import Flask, jsonify, request, redirect, url_for, render_template

from constants.tasks import NO_TASK
from fake import Profile
from constants.products import PRODUCTS, NO_PRODUCTS

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["JSON_SORT_KEYS"] = False


@app.route("/")
def index():
    return "Home"


@app.route("/products", strict_slashes=False)
def products():
    return PRODUCTS


@app.route("/products/<int:_id>", strict_slashes=False)
def get_product(_id):
    for product in PRODUCTS:
        if product.get("id") == _id:
            return product
    return NO_PRODUCTS


@app.route("/health")
def health_check():
    return "<h3>Health is Ok</h3>"


@app.route("/profile/", strict_slashes=False)
@app.route("/me/")
@app.route("/mine/")
def mine():
    return f"Hello '{os.getlogin().title()}'"


@app.route("/profiles/<int:_id>/")
def get_profile(_id):
    return jsonify(
        {
            "id": _id,
            "name": os.getlogin(),
            "addresses": [
                {"street": "5", "city": "October", "state": "Hosary"},
                {"street": "4", "city": "Zayed", "state": "Hyper"},
            ],
            "hobbies": ["Football", "Reading", "coding"],
        }
    )


@app.route("/profiles/", strict_slashes=False, methods=["POST", "PUT"])
def profiles():
    return jsonify(Profile().to_json()), HTTPStatus.CREATED


@app.route("/welcome/<string:name>/", strict_slashes=False)
@app.route(
    "/welcome/", strict_slashes=False, defaults={"name": os.getlogin()}
)  # default params values
def welcome(name):
    return "Welcome '{}'".format(name)


@app.route("/items/")
def items():
    args = request.args
    if not args:
        return NO_PRODUCTS
    return jsonify(args)


@app.route("/login/", strict_slashes=False, methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username and password:
            return redirect(url_for("mine"))  # method of redirect
    return render_template("login.html")  # render html page


@app.route("/signup/", methods=["GET", "POST"])
def signup():
    _id = random.randint(1, 10)
    if request.method == "POST":
        return redirect(url_for("get_profile", _id=_id))
    return render_template("signup.html")


@app.route("/tasks/", methods=["POST"])
def create_task():
    # try with postman to add json body and capture it
    # task = request.get_json() ==> equal ==>  task = request.json
    if not request.data:  # check if json data provided to the request
        return NO_TASK
    task = request.json
    if not task:
        return NO_TASK
    task.update({"created_at": datetime.now()})
    return jsonify(task), HTTPStatus.CREATED


def is_ended(nums, i):
    return i == len(nums) - 1


def is_diff(current, _next):
    return current != _next


if __name__ == "__main__":
    app.run()
