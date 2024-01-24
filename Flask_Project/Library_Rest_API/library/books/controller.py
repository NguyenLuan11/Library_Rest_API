from flask import Blueprint
from .services import add_book_service, get_book_by_id_service, get_all_books_service, \
    update_book_by_id_service, delete_book_by_id_service, get_book_by_author_service, get_book_by_category_service
from flasgger import swag_from

books = Blueprint("books", __name__, url_prefix="/book-management")


# GET ALL BOOK
@books.route("/books", methods=['GET'])
@swag_from("docs/get_all_books.yaml")
def get_all_books():
    return get_all_books_service()


# ADD A NEW BOOK
@books.route("/book", methods=['POST'])
@swag_from("docs/add_book.yaml")
def add_book():
    return add_book_service()


# GET BOOK BY ID
@books.route("/book/<int:id>", methods=['GET'])
@swag_from("docs/get_book_by_id.yaml")
def get_book_by_id(id):
    return get_book_by_id_service(id)


# UPDATE BOOK BY ID
@books.route("/book/<int:id>", methods=['PUT'])
@swag_from("docs/update_book_by_id.yaml")
def update_book_by_id(id):
    return update_book_by_id_service(id)


# DELETE BOOK BY ID
@books.route("/book/<int:id>", methods=['DELETE'])
@swag_from("docs/delete_book_by_id.yaml")
def delete_book_by_id(id):
    return delete_book_by_id_service(id)


# GET BOOK BY AUTHOR
@books.route("/book/<string:author>", methods=['GET'])
@swag_from("docs/get_book_by_author.yaml")
def get_book_by_author(author):
    return get_book_by_author_service(author)


# GET BOOK BY CATEGORY
@books.route("/book/<string:category>", methods=['GET'])
@swag_from("docs/get_book_by_category.yaml")
def get_book_by_category(category):
    return get_book_by_category_service(category)
