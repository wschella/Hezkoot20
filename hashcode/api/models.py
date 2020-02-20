class Library():
    def __init__(self, id_, num_books, num_days, flow, books):
        self.id = id_
        self.num_books = num_books
        self.num_days = num_days
        self.flow = flow
        self.books = books


class Solution():

    def __init__(self):
        self.libraries = []

    def add_lib(self, id_, books):
        self.libraries.append(SolLib(id_, books))

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
