from book import Book
from library import Library
from student import Student

if __name__ == '__main__':
    library = Library()

    book1 = Book(1, 'George Orwell', '1984')
    book2 = Book(2, 'George Orwell', 'Animal Farm')
    book3 = Book(3, 'Sir Arthur Conan Doyle', 'A Study in Scarlet')
    book4 = Book(4, 'Sun Szu', 'The Art of War')
    book5 = Book(5, 'Not-owned-book', 'No one')

    student1 = Student(1, 'Alice')
    student2 = Student(2, 'Bob')
    student3 = Student(3, "John")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    library.display_books()

    library.add_student(student1)
    library.add_student(student2)
    library.add_student(student3)
    library.display_students()

    library.lend_book(book1, student1)
    library.lend_book(book2, student3)
    library.return_book(book2, student3)
    library.lend_book(book4, student2)

    library.search_books([1, 2], 'id')
    library.search_books(['Bruce Wayne'], 'title')
