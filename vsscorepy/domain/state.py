from random import randint

from vsscorepy.domain.ball import Ball
from vsscorepy.domain.robot import Robot


class State(object):

    def __init__(self, ball: Ball = Ball(), team_blue: list = list(), team_yellow: list = list()):
        self.ball = ball
        self.team_blue = team_blue
        self.team_yellow = team_yellow

    def clean(self):
        self.ball = Ball()
        self.team_blue = list()
        self.team_yellow = list()

    @classmethod
    def random(cls):
        ball = Ball.random()
        qtd_yellow = randint(2, 10)
        qtd_blue = randint(2, 10)

        team_yellow = [Robot.random() for i in range(1, qtd_yellow)]
        team_blue = [Robot.random() for i in range(1, qtd_blue)]

        return cls(ball=ball, team_blue=team_blue, team_yellow=team_yellow)
