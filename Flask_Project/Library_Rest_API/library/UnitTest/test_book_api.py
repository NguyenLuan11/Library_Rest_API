import unittest
import requests

BASE_URL = "http://127.0.0.1:5000/book-management/"
URL_GET_DELETE_UPDATE_BOOK_BY_ID_BY_AUTHOR = BASE_URL + "book/"
URL_GET_ALL_BOOK = BASE_URL + "books"


class TestBookAPI(unittest.TestCase):
    # Positive
    def test_get_all_books(self):
        response = requests.get(URL_GET_ALL_BOOK)
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.json()), 0)

    def test_get_book_by_id(self):
        id_book = "1"
        response = requests.get(URL_GET_DELETE_UPDATE_BOOK_BY_ID_BY_AUTHOR + id_book)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 5)

    def test_get_book_by_author(self):
        author_name = "Phạm Huy Hoàng"
        response = requests.get(URL_GET_DELETE_UPDATE_BOOK_BY_ID_BY_AUTHOR + author_name)
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.json()), 1)

    # Negative
    def test_get_book_by_id_negative(self):
        id_book = "100"
        response = requests.get(URL_GET_DELETE_UPDATE_BOOK_BY_ID_BY_AUTHOR + id_book)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(len(response.json()), 1)

# RUN TEST: python -m unittest __file_name__.py
