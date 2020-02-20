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

    def print(self, file=None):
        if file:
            file = open(file, 'w')

        print(len(self.libraries), file=file)

        for lib in self.libraries:
            print("{} {}".format(lib.id, len(lib.books)), file=file)
            print(" ".join([str(b) for b in lib.books]), file=file)


class SolLib():
    def __init__(self, id_, books):
        self.id = id_
        self.books = books
