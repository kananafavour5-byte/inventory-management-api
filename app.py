from flask import Flask, jsonify, request
from inventory import inventory
from openfood import get_product

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Inventory Management API is running"
    })


@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(inventory)


@app.route("/inventory/<int:item_id>", methods=["GET"])
def get_item(item_id):

    item = next(
        (
            product for product in inventory
            if product["id"] == item_id
        ),
        None
    )

    if item:
        return jsonify(item)

    return jsonify({
        "error": "Item not found"
    }), 404

@app.route("/inventory", methods=["POST"])
def add_item():

    data = request.json

    new_item = {
        "id": len(inventory) + 1,
        "barcode": data["barcode"],
        "product_name": data["product_name"],
        "brand": data["brand"],
        "price": data["price"],
        "stock": data["stock"]
    }

    inventory.append(new_item)

    return jsonify(new_item), 201

@app.route("/inventory/<int:item_id>", methods=["PATCH"])
def update_item(item_id):

    item = next(
        (product for product in inventory
         if product["id"] == item_id),
        None
    )

    if not item:
        return jsonify({
            "error": "Item not found"
        }), 404

    data = request.json

    item.update(data)

    return jsonify(item)

@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):

    item = next(
        (product for product in inventory
         if product["id"] == item_id),
        None
    )

    if not item:
        return jsonify({
            "error": "Item not found"
        }), 404

    inventory.remove(item)

    return jsonify({
        "message": "Item deleted successfully"
    })

@app.route("/food/<barcode>", methods=["GET"])
def search_food(barcode):

    product = get_product(barcode)

    if product:
        return jsonify(product)

    return jsonify({
        "error": "Product not found"
    }), 404

if __name__ == "__main__":
    app.run(debug=True)
