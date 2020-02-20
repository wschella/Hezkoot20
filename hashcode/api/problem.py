from hashcode.api.models import Library

EXAMPLE = 'todo.in'
EASY = 'todo.in'
NO_HURRY = 'todo.in'
METRO = 'todo.in'
BONUS = 'todo.in'


class Problem:
    def __init__(self, problem):
        self.libraries = []

        with open('{}'.format(problem)) as file:
            num_books, num_libs, num_days = [int(x) for x in next(file).split()]

            self.numb_books = num_books
            self.num_libs = num_libs
            self.num_days = num_days

            weights = [int(x) for x in next(file).split()]
            assert len(weights) == num_books
            self.weights = weights

            for i in range(0, num_libs):
                lib_num_books, lib_days, lib_book_ships = [int(x) for x in next(file).split()]
                books = [int(x) for x in next(file).split()]
                assert len(books) == lib_num_books

                library = Library(i, lib_num_books, lib_days, lib_book_ships, books)
                self.libraries.append(library)

    def books_to_libs(self):
        books_to_libraries = [[] for _i in range(self.numb_books)]
        for library in self.libraries:
            for book in library.books:
                books_to_libraries[book].append(library)
        return books_to_libraries
