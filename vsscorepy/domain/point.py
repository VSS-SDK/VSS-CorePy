from random import randint


class Point:
    x = 0.0
    y = 0.0 

    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y

    @classmethod
    def random(cls):
        x = float(randint(0, 10))
        y = float(randint(0, 10))

        return cls(x=x, y=y)
