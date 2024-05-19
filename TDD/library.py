from book import Book
from student import Student


class Library:
    def __init__(self):
        self.books = list()
        self.students = list()

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise 'Not a Book'

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
        else:
            raise 'Not a Student'

    def lend_book(self, book, student):
        if book not in self.books:
            print(str(book) + ' not registered.')
            return False
        if student not in self.students:
            print(str(student) + ' not registered.')
            return False
        if book in student.books:
            print(str(student) + ' already has ' + str(book))
            return False
        self.books.remove(book)
        student.books.append(book)
        print(str(book) + ' lent to ' + str(student) + '.')
        return True

    def return_book(self, book, student):
        if student not in self.students:
            print(str(student) + ' not registered.')
            return False
        if not student.has_book(book):
            print(str(student) + ' does\'nt have' + str(book) + '.')
            return False
        self.books.append(book)
        student.books.remove(book)
        return True

    def search_students(self, keys, search_by):
        if search_by not in ('name', 'id'):
            raise 'You can only search by name or id'
        results = list()
        for student in self.students:
            if search_by == 'name' and student.name in keys:
                results.append(student)
            elif search_by == 'id' and student.id in keys:
                results.append(student)
        return results

    def search_books(self, keys, search_by):
        if search_by not in ('title', 'author', 'id'):
            raise 'You can only search by title, author or id'
        results = list()
        for book in self.books:
            if search_by == 'title' and book.title in keys:
                results.append(book)
            elif search_by == 'author' and book.author in keys:
                results.append(book)
            elif search_by == 'id' and book.id in keys:
                results.append(book)
        return results

    def display_books(self):
        print('Available books in library:')
        for book in self.books:
            print(book)

    def display_students(self):
        print('Registered students:')
        for student in self.students:
            print(student)
