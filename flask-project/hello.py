from flask import Flask, jsonify, request
from productos import products, IDGenerator, allowed_keys

generator = IDGenerator()

app = Flask(__name__)
@app.route('/', methods=['POST'])
def hello():
    print(request.json)
    return jsonify(products)

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify({"products":products})
@app.route('/product/<int:number>', methods=['GET'])
def get_a_product(number):
    product = next((p for p in products if p["id"] == number), None)
    return jsonify({"product": product})
@app.route('/products', methods=['POST'])
def add_product():
    print(request.json)
    product = {
        "category": request.json['category'],
        "description":request.json['description'],
        "id":generator.generate_id(),
        "image_url": request.json["image_url"],
        "name": request.json['name'],
        "price":request.json['price'],
        "stock":request.json['stock']
    }
    products.append(product)
    return jsonify({"product": "product"})
@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = next((p for p in products if p["id"] == id), None)
    products.remove(product)
    return jsonify({"product":product})

@app.route('/products/<int:id>', methods=['PUT', 'PATCH'])
def modify_product(id):
    product_index = next((i for i, p in enumerate(products) if p["id"] == id), None)
    filter_object = {key: value for key, value in request.json.items() if key in allowed_keys}
    products[product_index]["name"] = filter_object["name"]
    print(product_index)
    return jsonify({"product":"ciao"})


if __name__ == "__main__":
    app.run(port=4000, debug=True)