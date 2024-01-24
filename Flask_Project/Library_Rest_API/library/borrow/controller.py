from flask import Blueprint
from.services import add_borrow_service, update_borrow_by_id_service, \
    get_borrow_by_id_service, get_all_borrow_service, delete_borrow_by_id_service, get_borrow_book_author_category_service
from flasgger import swag_from

borrow = Blueprint("borrow", __name__, url_prefix="/borrow-management")


# ADD A NEW BORROW
@borrow.route("/borrow", methods=['POST'])
@swag_from("docs/add_borrow.yaml")
def add_borrow():
    return add_borrow_service()


# UPDATE BORROW
@borrow.route("/borrow/<int:id>", methods=['PUT'])
@swag_from("docs/update_borrow.yaml")
def update_borrow(id):
    return update_borrow_by_id_service(id)


# GET BORROW BY ID
@borrow.route("/borrow/<int:id>", methods=['GET'])
@swag_from("docs/get_borrow_by_id.yaml")
def get_borrow_by_id(id):
    return get_borrow_by_id_service(id)


# GET ALL BORROW
@borrow.route("/borrows", methods=['GET'])
@swag_from("docs/get_all_borrow.yaml")
def get_all_borrow():
    return get_all_borrow_service()


# DELETE BORROW BY ID
@borrow.route("/borrow/<int:id>", methods=['DELETE'])
@swag_from("docs/delete_borrow_by_id.yaml")
def delete_borrow_by_id(id):
    return delete_borrow_by_id_service(id)


# GET BORROW, BOOK, AUTHOR, CATEGORY BY STUDENT'S NAME
@borrow.route("/borrow/<string:student>", methods=['GET'])
@swag_from("docs/get_borrow_book_author_category.yaml")
def get_borrow_book_author_category(student):
    return get_borrow_book_author_category_service(student)
