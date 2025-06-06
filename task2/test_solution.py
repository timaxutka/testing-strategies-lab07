import unittest
from task2.solution import Book

class TestBook(unittest.TestCase):
    def test_is_long(self):
        self.assertTrue(Book("War and Peace", "Tolstoy", 1225).is_long())
        self.assertFalse(Book("Short Book", "Author", 120).is_long())

    def test_get_info(self):
        book = Book("1984", "Orwell", 328)
        self.assertEqual(book.get_info(), "Название: 1984, Автор: Orwell")

if __name__ == "__main__":
    unittest.main(verbosity=2)
