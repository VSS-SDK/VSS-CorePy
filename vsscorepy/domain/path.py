from random import randint

from vsscorepy.domain.point import Point


class Path(object):

    def __init__(self, points: list = list()):
        self.points = points

    def clean(self):
        self.points = list()

    @classmethod
    def random(cls):
        qtd_points = randint(2, 10)

        points = [Point.random() for i in range(1, qtd_points)]

        return cls(points=points)

    def __eq__(self, other):
        if len(self.points) is not len(other.points):
            return False

        for i in range(0, len(other.points)):
            if other.points[i] != self.points[i]:
                return False

        return True

    def __ne__(self, other):
        return not self.__eq__(other)

