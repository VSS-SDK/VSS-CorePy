from vsscorepy.domain.state import State
from vsscorepy.domain.ball import Ball
from vsscorepy.domain.robot import Robot
from vsscorepy.protos.state_pb2 import Global_State


class StateMapper(object):

    @classmethod
    def global_state_to_state(cls, global_state=Global_State()):
        state = State()

        state.ball = cls.__get_ball(global_state)
        state.team_blue = cls.__get_team_blue(global_state)
        state.team_yellow = cls.__get_team_yellow(global_state)

        return state

    @classmethod
    def __get_ball(cls, global_state):
        ball_state = global_state.balls[0]
        ball_pose = ball_state.pose
        ball_v_pose = ball_state.v_pose

        ball = Ball(ball_pose.x, ball_pose.y, ball_v_pose.x, ball_v_pose.y)
        return ball

    @classmethod
    def __get_team_blue(cls, global_state):
        team_blue = list()

        robots = global_state.robots_blue

        for robot_state in robots:
            team_blue.append(cls.__get_robot(robot_state))

        return team_blue

    @classmethod
    def __get_team_yellow(cls, global_state):
        team_yellow = list()

        robots = global_state.robots_yellow

        for robot_state in robots:
            team_yellow.append(cls.__get_robot(robot_state))

        return team_yellow

    @classmethod
    def __get_robot(cls, robot_state):
        robot_pose = robot_state.pose
        robot_v_pose = robot_state.v_pose

        return Robot(robot_pose.x, robot_pose.y, robot_pose.yaw, robot_v_pose.x, robot_v_pose.y, robot_v_pose.yaw)
