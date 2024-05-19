import unittest
from library import Library
from book import Book
from student import Student


class SearchTestCase(unittest.TestCase):
    def test_book_search(self):
        # Arrange
        library = Library()

        book1 = Book(1, 'George Orwell', '1984')
        book2 = Book(2, 'George Orwell', 'Animal Farm')
        book3 = Book(3, 'Sir Arthur Conan Doyle', 'A Study in Scarlet')
        book4 = Book(4, 'Sun Szu', 'The Art of War')
        book5 = Book(5, 'Sir Arthur Conan Doyle', 'The Sign of Four')

        # Act
        library.add_book(book1)
        library.add_book(book2)
        library.add_book(book3)
        library.add_book(book4)

        author_search = library.search_books(['George Orwell'], 'author')
        id_search = library.search_books([1, 2, 3], 'id')
        title_search = library.search_books(['The Great Gatsby', 'Catch-22'], 'title')

        # Assert
        self.assertFalse(book5 in library.books, 'unregistered book')
        self.assertListEqual(author_search, [book1, book2], 'search by author')
        self.assertListEqual(id_search, [book1, book2, book3], 'search by id')
        self.assertListEqual(title_search, list(), 'search by title')

    def test_student_search(self):
        # Arrange
        library = Library()

        student1 = Student(1, 'Alice')
        student2 = Student(2, 'Bob')
        student3 = Student(3, "John")

        # Act
        library.add_student(student1)
        library.add_student(student2)
        library.add_student(student3)

        id_search = library.search_students([1, 2], 'id')
        name_search = library.search_students(['Alice', 'Bob', 'David'], 'name')

        # Assert
        self.assertListEqual(id_search, [student1, student2], 'search by id')
        self.assertListEqual(name_search, [student1, student2], 'search by name')


class LendingTestCase(unittest.TestCase):
    def test_lending(self):
        # Arrange
        library = Library()

        book1 = Book(1, 'George Orwell', '1984')
        book2 = Book(2, 'George Orwell', 'Animal Farm')
        book3 = Book(3, 'Sir Arthur Conan Doyle', 'A Study in Scarlet')
        book4 = Book(4, 'Sun Szu', 'The Art of War')
        book5 = Book(5, 'Not-owned-book', 'No one')

        student1 = Student(1, 'Alice')
        student2 = Student(2, 'Bob')
        student3 = Student(3, "John")
        student4 = Student(4, "David")

        # Act
        library.add_book(book1)
        library.add_book(book2)
        library.add_book(book3)
        library.add_book(book4)
        library.display_books()

        library.add_student(student1)
        library.add_student(student2)
        library.add_student(student3)

        # Assert
        self.assertTrue(library.lend_book(book1, student1), 'lending')
        self.assertTrue(library.return_book(book1, student1), 'returning')
        self.assertTrue(library.lend_book(book1, student3), 're-lending')
        self.assertFalse(library.lend_book(book5, student3), 'book not registered')
        self.assertFalse(library.lend_book(book1, student2), 'already lent')
        self.assertTrue(library.return_book(book1, student3), 'returning')
        self.assertFalse(library.return_book(book4, student2), 'don\'t have book')
        self.assertFalse(library.lend_book(book2, student4), 'student not registered')


if __name__ == '__main__':
    unittest.main()
