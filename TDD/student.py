class Student:
    def __init__(self, std_id, name):
        self.name = name
        self.id = std_id
        self.books = list()

    def has_book(self, book):
        return book in self.books

    def display_books(self):
        print(self + ' has these books:')
        for book in self.books:
            print(book)

    def __str__(self):
        return self.name + '|' + str(self.id)

    def __repr__(self):
        return self.name + '|' + str(self.id)
