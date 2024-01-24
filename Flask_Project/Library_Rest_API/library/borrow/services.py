from ..extension import db
from ..model import Borrow, Books, Author, Category, Students
from ..library_ma import BorrowSchema
from flask import request, jsonify
import json
from datetime import date
from sqlalchemy.sql import func

borrow_schema = BorrowSchema()
borrows_schema = BorrowSchema(many=True)


def add_borrow_service():
    data = request.json
    if data and ('book_id' in data) and ('student_id' in data) and ('borrow_date' in data) and ('return_date' in data):
        book_id = data['book_id']
        student_id = data['student_id']
        borrow_date_list = data['borrow_date'].split('-')
        borrow_date = date(int(borrow_date_list[0]), int(borrow_date_list[1]), int(borrow_date_list[2]))
        return_date_list = data['return_date'].split('-')
        return_date = date(int(return_date_list[0]), int(return_date_list[1]), int(return_date_list[2]))
        try:
            new_borrow = Borrow(book_id=book_id, student_id=student_id, borrow_date=borrow_date, return_date=return_date)
            db.session.add(new_borrow)
            db.session.commit()

            book = Books.query.get(new_borrow.book_id)
            student = Students.query.get(new_borrow.student_id)

            return jsonify({"message": "Added success!",
                            "borrow": {"id": new_borrow.id,
                                       "book": book.name,
                                       "student": student.name,
                                       "borrow_date": new_borrow.borrow_date.strftime("%Y-%m-%d"),
                                       "return_date": new_borrow.return_date.strftime("%Y-%m-%d")}
                            }), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Can not add borrow!"}), 400
    else:
        return jsonify({"message": "Request error!"}), 400


def update_borrow_by_id_service(id):
    borrow = Borrow.query.get(id)
    data = request.json
    if borrow:
        if data and ('borrow_date' in data) and ('return_date' in data):
            try:
                borrow_date_list = data['borrow_date'].split('-')
                borrow_date = date(int(borrow_date_list[0]), int(borrow_date_list[1]), int(borrow_date_list[2]))
                return_date_list = data['return_date'].split('-')
                return_date = date(int(return_date_list[0]), int(return_date_list[1]), int(return_date_list[2]))

                borrow.borrow_date = borrow_date
                borrow.return_date = return_date
                db.session.commit()

                book = Books.query.get(borrow.book_id)
                student = Students.query.get(borrow.student_id)

                return jsonify({"message": "Borrow updated!",
                                "borrow": {"id": borrow.id,
                                           "book": book.name,
                                           "student": student.name,
                                           "borrow_date": borrow.borrow_date.strftime("%Y-%m-%d"),
                                           "return_date": borrow.return_date.strftime("%Y-%m-%d")}
                                }), 200
            except IndentationError:
                db.session.rollback()
                return jsonify({"message": "Can not update borrow!"}), 400
    else:
        return jsonify({"message": "Not found borrow!"}), 404


def get_borrow_by_id_service(id):
    borrow = Borrow.query.get(id)
    if borrow:
        book = Books.query.get(borrow.book_id)
        student = Students.query.get(borrow.student_id)

        return jsonify({"id": borrow.id,
                        "book": book.name,
                        "student": student.name,
                        "borrow_date": borrow.borrow_date.strftime("%Y-%m-%d"),
                        "return_date": borrow.return_date.strftime("%Y-%m-%d")}), 200
    else:
        return jsonify({"message": "Not found borrow!"}), 404


def get_all_borrow_service():
    borrows = Borrow.query.all()
    if borrows:
        borrows_list = []
        for borrow in borrows:
            book = Books.query.get(borrow.book_id)
            student = Students.query.get(borrow.student_id)

            borrows_list.append({
                "id": borrow.id,
                "book": book.name,
                "student": student.name,
                "borrow_date": borrow.borrow_date.strftime("%Y-%m-%d"),
                "return_date": borrow.return_date.strftime("%Y-%m-%d")
            })

        return jsonify(borrows_list), 200
    else:
        return jsonify({"message": "Not found list of borrow!"}), 404


def delete_borrow_by_id_service(id):
    borrow = Borrow.query.get(id)
    if borrow:
        try:
            db.session.delete(borrow)
            db.session.commit()
            return jsonify({"message": "Borrow deleted!"}), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Can not delete borrow!"}), 400
    else:
        return jsonify({"message": "Not found borrow!"}), 404


def get_borrow_book_author_category_service(student):
    borrows = db.session.query(Borrow.id, Books.name, Category.name, Author.name).join(
        Students, Borrow.student_id == Students.id).join(Books, Borrow.book_id == Books.id).join(
        Category, Category.id == Books.category_id).join(Author, Author.id == Books.author_id).filter(
        func.lower(Students.name) == student.lower()).all()
    if borrows:
        borrows_list = [{"id": row[0], "book": row[1], "category": row[2], "author": row[3]}
                        for row in borrows]
        return jsonify({f"{student} borrowed": borrows_list}), 200
    else:
        return jsonify({"message": "Not found borrow!"}), 404
