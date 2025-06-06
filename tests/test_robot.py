import unittest
from task2.solution import Book

class TestBookRobot(unittest.TestCase):
    def test_robot_book(self):
        book = Book("Robots", "Asimov", 400)
        self.assertTrue(book.is_long())
        self.assertIn("Asimov", book.get_info())
