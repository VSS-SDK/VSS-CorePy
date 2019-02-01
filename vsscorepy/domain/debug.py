class Debug(object):
    step_points = None
    final_poses = None
    paths = None

    def __init__(self, step_points: list = None, final_poses: list = None, paths: list = None):
        self.step_points = step_points
        self.final_poses = final_poses
        self.paths = paths

    def clean(self):
        self.step_points = list()
        self.final_poses = list()
        self.paths = list()
