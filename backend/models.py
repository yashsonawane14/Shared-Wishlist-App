from extensions import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(200))  # hashed or plain for mock
    wishlists = db.relationship('Wishlist', backref='owner', lazy=True)

class Wishlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    products = db.relationship('Product', backref='wishlist', lazy=True)
    
class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    image_url = db.Column(db.String(500))
    price = db.Column(db.Float)
    wishlist_id = db.Column(db.Integer, db.ForeignKey('wishlist.id'))
    added_by = db.Column(db.Integer, db.ForeignKey('user.id'))    
    added_at = db.Column(db.DateTime, default=datetime.utcnow)
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'image_url': self.image_url,
            'price': self.price,
            'wishlist_id': self.wishlist_id,
            'added_by': self.added_by
        }