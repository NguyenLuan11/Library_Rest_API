from flask import Flask, jsonify
from .books.controller import books
from .students.controller import students
from .borrow.controller import borrow
from .category_author.controller import category, author
from .user.controller import user
from .extension import db, ma
import os
from flask_jwt_extended import JWTManager
from flasgger import Swagger, swag_from
from .swagger import template, swagger_config


def create_app(config_file="config.py"):
    app = Flask(__name__)

    # Add file config
    app.config.from_pyfile(config_file)

    # Init Marshmallow
    ma.init_app(app)

    # Init DB
    db.init_app(app)

    # Create DB
    if not os.path.exists("/library/library.db"):
        with app.app_context():
            db.create_all()
            print("Created DB!")

    # JWT
    JWTManager(app)

    # Register BluePrint
    app.register_blueprint(books)
    app.register_blueprint(students)
    app.register_blueprint(borrow)
    app.register_blueprint(category)
    app.register_blueprint(author)
    app.register_blueprint(user)
    print(app.config["SECRET_KEY"])

    # Swagger
    Swagger(app, config=swagger_config, template=template)

    @app.errorhandler(404)
    def handle_404(e):
        return jsonify({'error': 'Not found'}), 404

    @app.errorhandler(500)
    def handle_500(e):
        return jsonify({'error': 'Something went wrong, we are working on it'}), 500

    return app
