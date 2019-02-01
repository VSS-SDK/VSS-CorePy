from vsscorepy.domain.pose import Pose


def test_rand_should_create_an_valid_object():
    pose = Pose.random()

    assert pose is not None
    assert pose.x is not None
    assert pose.y is not None
    assert pose.angle is not None


def test_default_constructor_should_create_zero_object():
    pose = Pose()

    assert pose is not None
    assert pose.x == 0
    assert pose.y == 0
    assert pose.angle == 0


def test_filled_constructor_should_create_valid_object():
    random = Pose.random()

    pose = Pose(x=random.x, y=random.y, angle=random.angle)

    assert pose is not None
    assert pose.x == random.x
    assert pose.y == random.y
    assert pose.angle == random.angle
