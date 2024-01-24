from ..extension import db
from ..model import Category, Author
from ..library_ma import CategorySchema, AuthorSchema
from flask import request, jsonify
import json

# CATEGORY
category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)


def add_category_service():
    data = request.json
    if data and ('name' in data):
        name = data['name']
        try:
            new_category = Category(name=name)
            db.session.add(new_category)
            db.session.commit()
            return jsonify({"message": "Added success!",
                           "category": {"id": new_category.id,
                                        "name": new_category.name}
                            }), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Can not add category!"}), 400
    else:
        return jsonify({"message": "Request error!"}), 400


def update_category_service(id):
    category = Category.query.get(id)
    data = request.json
    if category:
        if data and ('name' in data):
            try:
                category.name = data['name']
                db.session.commit()
                return jsonify({"message": "Category updated!",
                                "category": {"id": category.id,
                                             "name": category.name}
                                }), 200
            except IndentationError:
                db.session.rollback()
                return jsonify({"message": "Can not update category!"}), 400
    else:
        return jsonify({"message": "Not found Category!"}), 404


def get_category_by_id_service(id):
    category = Category.query.get(id)
    if category:
        return category_schema.jsonify(category), 200
    else:
        return jsonify({"message": "Not found Category!"}), 404


def get_all_category_service():
    categories = Category.query.all()
    if categories:
        return categories_schema.jsonify(categories), 200
    else:
        return jsonify({"message": "Not found list of Category!"}), 404


def delete_category_by_id_service(id):
    category = Category.query.get(id)
    if category:
        try:
            db.session.delete(category)
            db.session.commit()
            return jsonify({"message": "Category deleted!"}), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Can not delete category!"}), 400
    else:
        jsonify({"message": "Not found Category!"}), 404


# AUTHOR
author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)


def add_author_service():
    data = request.json
    if data and ('name' in data):
        name = data['name']
        try:
            new_author = Author(name=name)
            db.session.add(new_author)
            db.session.commit()
            return jsonify({"message": "Added success!",
                            "author": {"id": new_author.id,
                                       "name": new_author.name}
                            }), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Can not add author!"}), 400
    else:
        return jsonify({"message": "Request error!"}), 400


def update_author_service(id):
    author = Author.query.get(id)
    data = request.json
    if author:
        if data and ('name' in data):
            try:
                author.name = data['name']
                db.session.commit()
                return jsonify({"message": "Author updated!",
                                "author": {"id": author.id,
                                           "name": author.name}
                                }), 200
            except IndentationError:
                db.session.rollback()
                return jsonify({"message": "Can not update author!"}), 400
    else:
        return jsonify({"message": "Not found author!"}), 404


def get_author_by_id_service(id):
    author = Author.query.get(id)
    if author:
        return author_schema.jsonify(author), 200
    else:
        return jsonify({"message": "Not found author!"}), 404


def get_all_author_service():
    authors = Author.query.all()
    if authors:
        return authors_schema.jsonify(authors), 200
    else:
        return jsonify({"message": "Not found list of author!"}), 404


def delete_author_by_id_service(id):
    author = Author.query.get(id)
    if author:
        try:
            db.session.delete(author)
            db.session.commit()
            return jsonify({"message": "Author deleted!"}), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Can not delete author!"}), 400
    else:
        return jsonify({"message": "Not found author!"}), 404
