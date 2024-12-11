from flask import jsonify, request, Blueprint
from productos import products, IDGenerator, allowed_keys
from models.products import Products
from utils.db import db

generator = IDGenerator()

products_blueprint = Blueprint('products', __name__)

@products_blueprint.route('/products', methods=['GET'])
def get_products():
    productsDb = [
        {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "stock": product.stock,
        }
        for product in Products.query.all()
    ]
    print(productsDb)
    return jsonify({"products":productsDb})
@products_blueprint.route('/product/<int:id>', methods=['GET'])
def get_a_product(id):
    serialize_product = Products.query.get(id)
    product = {
            "id": serialize_product.id,
            "name": serialize_product.name,
            "description": serialize_product.description,
            "price": serialize_product.price,
            "stock": serialize_product.stock,
        }
    return jsonify({"product": product})
@products_blueprint.route('/products', methods=['POST'])
def add_product():
    print(request.json)
   
    newProduct = Products(
        description = request.json['description'],
        name = request.json['name'],
        price = request.json['price'],
        stock = request.json['stock']
    )
    
    db.session.add(newProduct)
    db.session.commit()
    
    print(newProduct)
    return jsonify({"product": "product"})
@products_blueprint.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Products.query.get(id)
    print(product)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"product":"deleted"})

@products_blueprint.route('/products/<int:id>', methods=['PUT', 'PATCH'])
def modify_product(id):
    product_index = next((i for i, p in enumerate(products) if p["id"] == id), None)
    filter_object = {key: value for key, value in request.json.items() if key in allowed_keys}
    products[product_index].update(filter_object)
    print(product_index)
    return jsonify({"product":"ciao"})
