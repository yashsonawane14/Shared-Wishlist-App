from flask import Flask
from flask_cors import CORS
from extensions import db, ma  # USE the shared db and ma
from routes.user import user_bp
from routes.wishlist import wl_bp
from routes.product import product_bp
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    CORS(app, origins="http://localhost:8080")

    # Configure app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/wishlist_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions with app
    db.init_app(app)
    ma.init_app(app)
    migrate = Migrate(app, db)

    # Register blueprints
    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(wl_bp, url_prefix='/api/wishlists')
    app.register_blueprint(product_bp, url_prefix='/api/products')

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
