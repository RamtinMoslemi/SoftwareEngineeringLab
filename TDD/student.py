class Student:
    def __init__(self, std_id: int, name: str):
        self.name = name
        self.id = std_id
        self.books = list()

    def has_book(self, book) -> bool:
        return book in self.books

    def display_books(self):
        print(self.__str__() + ' has these books:')
        for book in self.books:
            print(book)

    def __str__(self):
        return self.name + '|' + str(self.id)

    def __repr__(self):
        return self.name + '|' + str(self.id)
