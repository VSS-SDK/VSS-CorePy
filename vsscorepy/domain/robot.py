from random import randint

from vsscorepy.domain.pose import Pose


class Robot(Pose):
    speed_x = 0.0
    speed_y = 0.0
    speed_angle = 0.0

    def __init__(self, x: float = 0.0, y: float = 0.0, angle: float = 0.0, speed_x: float = 0.0, speed_y: float = 0.0,
                 speed_angle: float = 0.0):

        super().__init__(x, y, angle)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.speed_angle = speed_angle

    @classmethod
    def random(cls):
        x = float(randint(0, 10))
        y = float(randint(0, 10))
        angle = float(randint(0, 10))
        speed_x = float(randint(0, 10))
        speed_y = float(randint(0, 10))
        speed_angle = float(randint(0, 10))

        return cls(x=x, y=y, angle=angle, speed_x=speed_x, speed_y=speed_y, speed_angle=speed_angle)
