from vsscorepy.domain.debug import Debug
from vsscorepy.domain.point import Point
from vsscorepy.protos.debug_pb2 import Global_Debug
from vsscorepy.protos.debug_pb2 import Pose


class DebugMapper(object):

    @classmethod
    def debug_to_global_debug(cls, debug=Debug()):
        global_debug = Global_Debug()

        for i in range(0, len(debug.step_points)):
            global_debug.step_poses.add()

            step_pose = cls.__get_step_pose(debug.step_points[i])
            global_debug.step_poses[i].x = step_pose.x
            global_debug.step_poses[i].y = step_pose.y

        for i in range(0, len(debug.final_poses)):
            global_debug.final_poses.add()

            final_pose = cls.__get_final_pose(debug.final_poses[i])
            global_debug.final_poses[i].x = final_pose.x
            global_debug.final_poses[i].y = final_pose.y
            global_debug.final_poses[i].yaw = final_pose.yaw

        return global_debug

    @classmethod
    def __get_step_pose(cls, step_point):
        pose = Pose()

        pose.x = step_point.x
        pose.y = step_point.y
        pose.yaw = 0

        return pose

    @classmethod
    def __get_final_pose(cls, final_pose):
        pose = Pose()

        pose.x = final_pose.x
        pose.y = final_pose.y
        pose.yaw = final_pose.angle

        return pose
