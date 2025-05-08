from flask import Blueprint, request, jsonify
from extensions import db
from models import Wishlist, User
from schemas import WishlistSchema

wl_bp = Blueprint('wishlist', __name__)
wishlist_schema = WishlistSchema()
wishlists_schema = WishlistSchema(many=True)

@wl_bp.route('/', methods=['GET'])
def get_all_wishlists():
    wishlists = Wishlist.query.all()
    return wishlists_schema.jsonify(wishlists)

@wl_bp.route('/', methods=['POST'])
def create_wishlist():
    data = request.json
    wishlist = Wishlist(name=data['name'], owner_id=data['owner_id'])
    db.session.add(wishlist)
    db.session.commit()
    return wishlist_schema.jsonify(wishlist)

@wl_bp.route('/<int:owner_id>', methods=['GET'])
def get_user_wishlists(owner_id):
    wishlists = Wishlist.query.filter_by(owner_id=owner_id).all()
    return wishlists_schema.jsonify(wishlists)

@wl_bp.route('/<int:id>', methods=['PUT'])
def update_wishlist(id):
    wishlist = Wishlist.query.get(id)
    if not wishlist:
        return jsonify({'message': 'Wishlist not found'}), 404
    data = request.json
    wishlist.name = data['name']
    db.session.commit()
    return wishlist_schema.jsonify(wishlist)

@wl_bp.route('/<int:id>', methods=['DELETE'])
def delete_wishlist(id):
    wishlist = Wishlist.query.get(id)
    db.session.delete(wishlist)
    db.session.commit()
    return jsonify({'message': 'Wishlist deleted'})
