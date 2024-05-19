class Book:
    def __init__(self, book_id, author, title):
        self.id = book_id
        self.author = author
        self.title = title

    def __str__(self):
        return self.title + ' by ' + self.author

    def __repr__(self):
        return self.title + ' by ' + self.author
