from ..extension import db
from ..library_ma import StudentSchema
from ..model import Students
from flask import request, jsonify
import json
from datetime import date, datetime

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)


def add_student_service():
    data = request.json
    if data and ('name' in data) and ('birth_date' in data) and ('gender' in data) and ('class_name' in data):
        name = data['name']
        date_list = data['birth_date'].split('-')
        birth_date = date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
        gender = data['gender']
        class_name = data['class_name']
        try:
            new_student = Students(name=name, birth_date=birth_date, gender=gender, class_name=class_name)
            db.session.add(new_student)
            db.session.commit()

            return jsonify({"message": "Added success!",
                            "student": {"id": new_student.id,
                                        "name": new_student.name,
                                        "birth_date": new_student.birth_date.strftime("%Y-%m-%d"),
                                        "gender": new_student.gender,
                                        "class_name": new_student.class_name}
                            }), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Can not add student!"}), 400
    else:
        return jsonify({"message": "Request error!"}), 400


def update_student_service(id):
    student = Students.query.get(id)
    data = request.json
    if student:
        if data and ('name' in data) and ('birth_date' in data) and ('gender' in data) and ('class_name' in data):
            try:
                student.name = data['name']
                date_list = data['birth_date'].split('-')
                birth_date = date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
                student.birth_date = birth_date
                student.gender = data['gender']
                student.class_name = data['class_name']
                db.session.commit()
                return jsonify({"message": "Student updated!",
                                "student": {"id": student.id,
                                            "name": student.name,
                                            "birth_date": student.birth_date.strftime("%Y-%m-%d"),
                                            "gender": student.gender,
                                            "class_name": student.class_name}
                                }), 200
            except IndentationError:
                db.session.rollback()
                return jsonify({"message": "Can not update student!"}), 400
    else:
        return jsonify({"message": "Not found student!"}), 404


def get_student_by_id_service(id):
    student = Students.query.get(id)
    if student:
        return student_schema.jsonify(student), 200
    else:
        return jsonify({"message": "Not found student!"}), 404


def get_all_student_service():
    students = Students.query.all()
    if students:
        return students_schema.jsonify(students), 200
    else:
        return jsonify({"message": "Not found list of students!"}), 404


def delete_student_by_id_service(id):
    student = Students.query.get(id)
    if student:
        try:
            db.session.delete(student)
            db.session.commit()
            return jsonify({"message": "Student deleted!"}), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Can not delete student!"}), 400
    else:
        return jsonify({"message": "Not found list of student!"}), 404
