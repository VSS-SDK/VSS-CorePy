from random import randint


class Point(object):
    x = None
    y = None

    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y

    @classmethod
    def random(cls):
        x = float(randint(0, 10))
        y = float(randint(0, 10))

        return cls(x=x, y=y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)
