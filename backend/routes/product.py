from flask import Blueprint, request, jsonify
from flask_cors import CORS
from extensions import db
from models import Product
from schemas import ProductSchema

product_bp = Blueprint("product", __name__, url_prefix="/api/products")

#product_bp = Blueprint('product', __name__)
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
CORS(product_bp, origins="http://localhost:8080", supports_credentials=True)  # Allow Vue frontend

@product_bp.route("/", methods=["GET"])
def get_all_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])
    
@product_bp.route("/", methods=["POST", "OPTIONS"])
def add_product():
    data = request.get_json()
    product = Product(
        name=data["name"],
        image_url=data["image_url"],
        price=data["price"],
        wishlist_id=data["wishlist_id"],
        added_by=data.get("added_by")     # <- safe lookup
    )
    db.session.add(product)
    db.session.commit()
    return product_schema.jsonify(product)

@product_bp.route('/<int:wishlist_id>', methods=['GET'])
def get_products(wishlist_id):
    products = Product.query.filter_by(wishlist_id=wishlist_id).all()
    return products_schema.jsonify(products)

@product_bp.route('/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get(id)
    data = request.json
    product.name = data['name']
    product.image_url = data['image_url']
    product.price = data['price']
    db.session.commit()
    return product_schema.jsonify(product)

@product_bp.route('/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted'})