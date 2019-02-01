from random import randint

from vsscorepy.domain.point import Point


class Ball(Point):
    speed_x = 0.0
    speed_y = 0.0

    def __init__(self, x=0.0, y=0.0, speed_x=0.0, speed_y=0.0):
        super().__init__(x, y)
        self.speed_x = speed_x
        self.speed_y = speed_y

    @classmethod
    def random(cls):
        x = float(randint(0, 10))
        y = float(randint(0, 10))
        speed_x = float(randint(0, 10))
        speed_y = float(randint(0, 10))

        return cls(x=x, y=y, speed_x=speed_x, speed_y=speed_y)
