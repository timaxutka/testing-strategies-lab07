from task1.solution import days_between_dates
from task2.solution import Book

print("📅 Разница в днях:")
print(days_between_dates("01.01.2020", "10.01.2020"))

print("\n📖 Работа с книгой:")
book = Book("Dune", "Frank Herbert", 412)
print("Долгая книга?", book.is_long())
print(book.get_info())
