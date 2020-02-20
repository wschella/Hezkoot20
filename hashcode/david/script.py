from hashcode.api.models import Library, Solution
from hashcode.api.problem import Problem
import numpy as np
import sys


def solve(problem):
    solution = Solution(problem)

    used_libs = set()
    days_left = problem.num_days

    while days_left > 0:
        print(days_left, file=sys.stderr)
        library = max(problem.libraries, key=lambda lib: score_library(
            lib, solution, problem, days_left, used_libs))
        used_libs.add(library)
        days_left -= library.num_days

        solution.add_lib(library)

    return solution


def score_library(library, solution, problem, days_left, used_libs):
    if library in used_libs:
        return 0

    if library.num_days >= days_left:
        return 0

    return solution.score_gained(library) / library.num_days ** 1.3


def solve_d(problem):
    books_to_libraries = [[] for _i in range(problem.numb_books)]
    for library in problem.libraries:
        for book in library.books:
            books_to_libraries[book].append(library)
    scanned = [False] * problem.numb_books

    library_scores = [len(library.books) for library in problem.libraries]
    day = 0
    print(problem.num_days // 2)
    while day < problem.num_days:
        print(day, file=sys.stderr)
        libraryId = np.argmax(library_scores)
        library = problem.libraries[libraryId]
        to_send = []
        for book in library.books:
            if scanned[book]:
                continue
            scanned[book] = True
            to_send.append(str(book))
            for lib2 in books_to_libraries[book]:
                library_scores[lib2.id] -= 1

        day += 2
        print(str(libraryId) + " " + str(len(to_send)))
        print(" ".join(to_send))
