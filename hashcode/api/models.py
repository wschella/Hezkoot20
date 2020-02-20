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

    def lib_score_add(self, lib):
        days_left = self.days_left - lib.num_days

        bbw = [(self.problem.weights[book], book)
               for book in lib.books if book not in self.found_books]
        bbw.sort()
        bbw.reverse()
        books = list(zip(*bbw))[1][:lib.flow * days_left]
        book_scores = [self.problem.weights[book] for book in books]
        return sum(book_scores)

    def add_lib(self, lib, books=None):
        self.days_left -= lib.num_days
        if books == None:
            bbw = [(self.problem.weights[book], book)
                   for book in lib.books if book not in self.found_books]
            if len(bbw) == 0:
                self.days_left += lib.num_days
                return
            bbw.sort()
            bbw.reverse()
            books = list(zip(*bbw))[1][:lib.flow * self.days_left]

        for book in books:
            self.found_books.add(book)

        self.libraries.append(SolLib(lib.id, books))

    def print(self, file=None):
        if file:
            file = open(file, 'w')

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
