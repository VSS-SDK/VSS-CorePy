from random import randint


class WheelsCommand(object):
    left_vel = None
    right_vel = None

    def __init__(self, left_vel: float = 0.0, right_vel: float = 0.0):
        self.left_vel = left_vel
        self.right_vel = right_vel

    @classmethod
    def random(cls):
        left_vel = float(randint(0, 10))
        right_vel = float(randint(0, 10))

        return cls(left_vel=left_vel, right_vel=right_vel)

    def __eq__(self, other):
        return self.left_vel == other.left_vel and self.right_vel == other.right_vel

    def __ne__(self, other):
        return not self.__eq__(other)
