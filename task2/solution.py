class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def is_long(self):
        return self.pages > 300

    def get_info(self):
        return f"Название: {self.title}, Автор: {self.author}"
