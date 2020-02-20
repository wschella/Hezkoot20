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

    def get_best_books(self, lib, time_left):
        bbw = [(self.problem.weights[book], book)
                for book in lib.books if book not in self.found_books]
        if len(bbw) == 0:
            return []
        bbw.sort()
        bbw.reverse()
        return list(zip(*bbw))[1][:lib.flow * time_left]


    def add_lib(self, lib, books=None):
        self.days_left -= lib.num_days
        if self.days_left <= 0:
            self.days = 0
            return
        if books == None:
            books = self.get_best_books(lib, self.days_left)
            if len(books) == 0:
                self.days_left += lib.num_days
                return

        for book in books:
            self.found_books.add(book)

        self.libraries.append(SolLib(lib.id, books))

    def score_gained(self, lib, books=None):
        if books == None:
            books = self.get_best_books(lib, self.days_left-lib.num_days)
        books = [book for book in books if book not in self.found_books][:self.days_left*lib.flow]
        return sum([self.problem.weights[book] for book in books])

    def print(self, file=None):
        if file:
            file = open(file, 'w')

        self.libraries = [lib for lib in self.libraries if len(lib.books) > 0]
        print(len(self.libraries), file=file)

        for lib in self.libraries:
            print("{} {}".format(lib.id, len(lib.books)), file=file)
            print(" ".join([str(b) for b in lib.books]), file=file)

    def score(self):
        return sum([self.problem.weights[book] for book in self.found_books])


class SolLib():
    def __init__(self, id_, books):
        self.id = id_
        self.books = books
