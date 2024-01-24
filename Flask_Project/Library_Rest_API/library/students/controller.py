from flask import Blueprint
from .services import add_student_service, update_student_service, get_all_student_service, \
    get_student_by_id_service, delete_student_by_id_service
from flasgger import swag_from

students = Blueprint("students", __name__, url_prefix="/students-management")


# ADD A NEW STUDENT
@students.route("/student", methods=['POST'])
@swag_from("docs/add_student.yaml")
def add_student():
    return add_student_service()


# UPDATE STUDENT
@students.route("/student/<int:id>", methods=['PUT'])
@swag_from("docs/update_student.yaml")
def update_student(id):
    return update_student_service(id)


# GET ALL STUDENT
@students.route("/students", methods=['GET'])
@swag_from("docs/get_all_student.yaml")
def get_all_student():
    return get_all_student_service()


# GET STUDENT BY ID
@students.route("/student/<int:id>", methods=['GET'])
@swag_from("docs/get_student_by_id.yaml")
def get_student_by_id(id):
    return get_student_by_id_service(id)


# DELETE STUDENT BY ID
@students.route("/student/<int:id>", methods=['DELETE'])
@swag_from("docs/delete_student_by_id.yaml")
def delete_student_by_id(id):
    return delete_student_by_id_service(id)
