from http import HTTPStatus
import os
from flask import Flask, jsonify, request
from fake import Profile
from constants.products import PRODUCTS, NO_PRODUCTS


app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(debug=True)
