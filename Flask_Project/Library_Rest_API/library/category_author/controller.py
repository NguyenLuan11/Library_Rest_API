from flask import Blueprint
from .services import add_category_service, update_category_service, get_all_category_service, \
    get_category_by_id_service, delete_category_by_id_service, \
    add_author_service, update_author_service, get_all_author_service, \
    get_author_by_id_service, delete_author_by_id_service
from flasgger import swag_from

# CATEGORY
category = Blueprint("category", __name__, url_prefix="/category-management")


# ADD A NEW CATEGORY
@category.route("/category", methods=['POST'])
@swag_from("docs/category/add_category.yaml")
def add_category():
    return add_category_service()


# UPDATE CATEGORY
@category.route("/category/<int:id>", methods=['PUT'])
@swag_from("docs/category/update_category.yaml")
def update_category(id):
    return update_category_service(id)


# GET CATEGORY BY ID
@category.route("/category/<int:id>", methods=['GET'])
@swag_from("docs/category/get_category_by_id.yaml")
def get_category_by_id(id):
    return get_category_by_id_service(id)


# GET ALL CATEGORY
@category.route("/categories", methods=['GET'])
@swag_from("docs/category/get_all_category.yaml")
def get_all_category():
    return get_all_category_service()


# DELETE CATEGORY BY ID
@category.route("/category/<int:id>", methods=['DELETE'])
@swag_from("docs/category/delete_category_by_id.yaml")
def delete_category_by_id(id):
    return delete_category_by_id_service(id)


# AUTHOR
author = Blueprint("author", __name__, url_prefix="/author-management")


# ADD A NEW AUTHOR
@author.route("/author", methods=['POST'])
@swag_from("docs/author/add_author.yaml")
def add_author():
    return add_author_service()


# UPDATE AUTHOR
@author.route("/author/<int:id>", methods=['PUT'])
@swag_from("docs/author/update_author.yaml")
def update_author(id):
    return update_author_service(id)


# GET AUTHOR BY ID
@author.route("/author/<int:id>", methods=['GET'])
@swag_from("docs/author/get_author_by_id.yaml")
def get_author_by_id(id):
    return get_author_by_id_service(id)


# GET ALL AUTHOR
@author.route("/authors", methods=['GET'])
@swag_from("docs/author/get_all_author.yaml")
def get_all_author():
    return get_all_author_service()


# DELETE AUTHOR BY ID
@author.route("/author/<int:id>", methods=['DELETE'])
@swag_from("docs/author/delete_author_by_id.yaml")
def delete_author_by_id(id):
    return delete_author_by_id_service(id)
