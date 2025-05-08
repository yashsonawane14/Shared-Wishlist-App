from flask import Blueprint, request, jsonify
from extensions import db
from models import User
from schemas import UserSchema

user_bp = Blueprint('user', __name__)
user_schema = UserSchema()

@user_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json

    name = data.get('name')
    email = data.get('email')
    firebase_uid = data.get('firebase_uid')

    if not name or not email or not firebase_uid:
        return jsonify({'message': 'Missing required fields'}), 400

    # Check if user already exists
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return user_schema.jsonify(existing_user), 200

    # Create and save new user
    new_user = User(username=name, email=email, password=firebase_uid)
    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user), 201

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    firebase_uid = data.get('firebase_uid')

    user = User.query.filter_by(email=email, password=firebase_uid).first()
    if not user:
        return jsonify({'message': 'Invalid credentials'}), 401
    return user_schema.jsonify(user), 200
