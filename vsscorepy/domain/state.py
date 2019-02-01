from vsscorepy.domain.ball import Ball


class State(object):
    ball = None
    team_blue = None
    team_yellow = None

    def __init__(self, ball: Ball = None, team_blue: list = None, team_yellow: list = None):
        self.ball = ball
        self.team_blue = team_blue
        self.team_yellow = team_yellow

    def clean(self):
        self.ball = Ball()
        self.team_blue = list()
        self.team_yellow = list()
