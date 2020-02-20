from hashcode.api.models import Photo

EXAMPLE = 'todo.in'
EASY = 'todo.in'
NO_HURRY = 'todo.in'
METRO = 'todo.in'
BONUS = 'todo.in'


class Problem:
    def __init__(self, problem):
        self.photos = []

        with open('{}'.format(problem)) as file:
            N = [int(x) for x in next(file).split()][0]
            self.N = N
            for i in range(0, N):
                line = [x for x in next(file).split()]
                n_tags = int(line[1])
                hor_Ver = line[0]
                tags = line[2:]
                photo = Photo(i, hor_Ver, n_tags, set(tags))
                self.photos.append(photo)

    def score(self, a, b):
        if isinstance(a, Photo):
            a = a.tags
        if isinstance(b, Photo):
            b = b.tags
        return min(len(a - b), len(b - a), len(a & b))

    def total_score(self, photos):
        s = 0
        for i in range(1, len(photos)):
            s += self.score(photos[i - 1], photos[i])
        return s
