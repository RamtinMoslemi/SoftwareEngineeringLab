class Book:
    def __init__(self, book_id: int, author: str, title: str):
        self.id = book_id
        self.author = author
        self.title = title

    def __str__(self):
        return self.title + ' by ' + self.author

    def __repr__(self):
        return f'{self.__class__.__name__}(id={self.id}, author={self.author}, title={self.title})'
