from random import randint

from vsscorepy.domain.point import Point


class Pose(Point):
    angle = None

    def __init__(self, x: float = 0.0, y: float = 0.0, angle: float = 0.0):
        super().__init__(x, y)
        self.angle = angle

    @classmethod
    def random(cls):
        x = float(randint(0, 10))
        y = float(randint(0, 10))
        angle = float(randint(0, 10))

        return cls(x=x, y=y, angle=angle)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.angle == other.angle

    def __ne__(self, other):
        return not self.__eq__(other)
