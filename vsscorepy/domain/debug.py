from random import randint

from vsscorepy.domain.path import Path
from vsscorepy.domain.point import Point
from vsscorepy.domain.pose import Pose


class Debug(object):

    def __init__(self, step_points: list = list(), final_poses: list = list(), paths: list = list()):
        self.step_points = step_points
        self.final_poses = final_poses
        self.paths = paths

    def clean(self):
        self.step_points = list()
        self.final_poses = list()
        self.paths = list()

    @classmethod
    def random(cls):
        qtd_step_points = randint(2, 10)
        qtd_final_poses = randint(2, 10)
        qtd_paths = randint(2, 10)

        step_points = [Point.random() for i in range(1, qtd_step_points)]
        final_poses = [Pose.random() for i in range(1, qtd_final_poses)]
        paths = [Path.random() for i in range(1, qtd_paths)]

        return cls(step_points=step_points, final_poses=final_poses, paths=paths)
