from ..extension import db
from ..library_ma import BookSchema
from ..model import Books, Author, Category
from flask import request, jsonify
from sqlalchemy.sql import func
import json

book_schema = BookSchema()
books_schema = BookSchema(many=True)


def add_book_service():
    data = request.json
    if data and ('name' in data) and ('page_count' in data) and ('author_id' in data) and ('category_id' in data):
        name = data['name']
        page_count = data['page_count']
        author_id = data['author_id']
        category_id = data['category_id']
        try:
            new_book = Books(name=name, page_count=page_count, author_id=author_id, category_id=category_id)
            db.session.add(new_book)
            db.session.commit()

            author = Author.query.get(new_book.author_id)
            category = Category.query.get(new_book.category_id)

            return jsonify({"message": "Added success!",
                            "book": {"id": new_book.id,
                                     "name": new_book.name,
                                     "page_count": new_book.page_count,
                                     "author": author.name,
                                     "category": category.name}
                            }), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Can not add book!"}), 400
    else:
        return jsonify({"message": "Request error!"}), 400


def get_book_by_id_service(id):
    book = Books.query.get(id)
    if book:
        author = Author.query.get(book.author_id)
        category = Category.query.get(book.category_id)

        return jsonify({"id": book.id,
                        "name": book.name,
                        "page_count": book.page_count,
                        "author": author.name,
                        "category": category.name}), 200
    else:
        return jsonify({"message": "Not found book!"}), 404


def get_all_books_service():
    books = Books.query.all()
    if books:
        books_list = []
        for book in books:
            author = Author.query.get(book.author_id)
            category = Category.query.get(book.category_id)
            # print(author.name + " - " + category.name)

            books_list.append({
                "id": book.id,
                "name": book.name,
                "page_count": book.page_count,
                "author": author.name,
                "category": category.name
            })

        return jsonify(books_list), 200
    else:
        return jsonify({"message": "Not found list of book!"}), 404


def update_book_by_id_service(id):
    book = Books.query.get(id)
    data = request.json
    if book:
        if data and ('page_count' in data) and ("author_id" in data) and ("category_id" in data):
            try:
                book.page_count = data['page_count']
                book.author_id = data['author_id']
                book.category_id = data['category_id']
                db.session.commit()

                author = Author.query.get(book.author_id)
                category = Category.query.get(book.category_id)

                return jsonify({"message": "Book updated!",
                                "book": {"id": book.id,
                                         "name": book.name,
                                         "page_count": book.page_count,
                                         "author": author.name,
                                         "category": category.name}
                                }), 200
            except IndentationError:
                db.session.rollback()
                return jsonify({"message": "Can not update book!"}), 400
    else:
        return jsonify({"message": "Not found book!"}), 404


def delete_book_by_id_service(id):
    book = Books.query.get(id)
    if book:
        try:
            db.session.delete(book)
            db.session.commit()
            return jsonify({"message": "Book deleted!"}), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Can not delete book!"}), 400
    else:
        return jsonify({"message": "Not found book!"}), 404


def get_book_by_author_service(author):
    books = Books.query.join(Author).filter(func.lower(Author.name) == author.lower()).all()
    if books:
        books_list = []
        for book in books:
            author = Author.query.get(book.author_id)
            category = Category.query.get(book.category_id)

            books_list.append({
                "id": book.id,
                "name": book.name,
                "page_count": book.page_count,
                "author": author.name,
                "category": category.name
            })

        return jsonify(books_list), 200
    else:
        return jsonify({"message": f"Not found books by {author}!"}), 404


def get_book_by_category_service(category):
    books = Books.query.join(Category).filter(func.lower(Category.name) == category.lower()).all()
    if books:
        books_list = []
        for book in books:
            author = Author.query.get(book.author_id)
            category = Category.query.get(book.category_id)

            books_list.append({
                "id": book.id,
                "name": book.name,
                "page_count": book.page_count,
                "author": author.name,
                "category": category.name
            })

        return jsonify(books_list), 200
    else:
        return jsonify({"message": f"Not found books of {category}!"}), 404
