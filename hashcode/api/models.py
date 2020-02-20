class Library():
    def __init__(self, id_, num_books, num_days, flow, books):
        self.id = id_
        self.num_books = num_books
        self.num_days = num_days
        self.flow = flow
        self.books = set(books)


class Solution():

    def __init__(self, problem):
        self.libraries = []
        self.problem = problem
        self.found_books = set()
        self.days_left = problem.num_days

    def add_lib(self, lib, books=None):
        self.days_left -= lib.num_days
        if books == None:
            bbw = [(self.problem.weights[book], books) for book in lib.books if book not in self.found_books]
            bbw.sort()
            bbw.reverse()
            books = list(zip(*bbw))[1][:lib.flow*self.days_left]

        for book in books:
            self.found_books.add(book)
        self.libraries.append(SolLib(lib.id, books))

    def print(self):
        num_of_libraries = 0
        print(num_of_libraries)

        for lib in self.libraries:
            print(lib.id)
            print(len(lib.books))
            print(" ".join(lib.books))


class SolLib():
    def __init__(self, id_, books):
        self.id = id_
        self.books = books
