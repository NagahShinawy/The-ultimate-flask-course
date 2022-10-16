from flask import Flask

app = Flask(__name__)
PRODUCTS = [
        {"id": 1, "title": "Labtop", "price": 234.89},
        {"id": 2, "title": "mobile", "price": 968.89},
        {"id": 3, "title": "coffee machine", "price": 3213.89},
        {"id": 4, "title": "bed", "price": 32.89},
    ]

NO_PRODUCTS = 'No Product(s)'


@app.route("/")
def index():
    return "Home"


@app.route("/products")
def products():
    return PRODUCTS


@app.route("/products/<int:_id>")
def get_product(_id):
    for product in PRODUCTS:
        if product.get("id") == _id:
            return product
    return NO_PRODUCTS


if __name__ == '__main__':
    app.run(debug=True)