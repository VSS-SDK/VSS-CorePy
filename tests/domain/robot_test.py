from vsscorepy.domain.robot import Robot


def test_rand_should_create_an_valid_object():
    robot = Robot.random()

    assert robot is not None
    assert robot.x is not None
    assert robot.y is not None
    assert robot.angle is not None
    assert robot.speed_x is not None
    assert robot.speed_y is not None
    assert robot.speed_angle is not None


def test_default_constructor_should_create_zero_object():
    robot = Robot()

    assert robot is not None
    assert robot.x == 0
    assert robot.y == 0
    assert robot.angle == 0
    assert robot.speed_x == 0
    assert robot.speed_y == 0
    assert robot.speed_angle == 0


def test_filled_constructor_should_create_valid_object():
    random = Robot.random()

    robot = Robot(x=random.x, y=random.y, angle=random.angle, speed_x=random.speed_x, speed_y=random.speed_y, speed_angle=random.speed_angle)

    assert robot is not None
    assert robot.x == random.x
    assert robot.y == random.y
    assert robot.angle == random.angle
    assert robot.speed_x == random.speed_x
    assert robot.speed_y == random.speed_y
    assert robot.speed_angle == random.speed_angle
