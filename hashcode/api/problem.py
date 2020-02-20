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
            B, L, D = [int(x) for x in next(file).split()]

            self.B = B
            self.L = L
            self.D = D

            S = [x for x in next(file).split()]
            assert len(S) == B

            for i in range(0, L):
                N, T, M = [int(x) for x in next(file).split()]
                books = [int(x) for x in next(file).split()]
                assert len(books) == N

                library = Library(N, T, M, books)
                self.libraries.append(library)

    def score(self, a, b):
        pass

    def total_score(self, photos):
        pass
