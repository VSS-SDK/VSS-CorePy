from vsscorepy.domain.point import Point


def test_rand_should_create_an_valid_object():
    point = Point.random()

    assert point is not None
    assert point.x is not None
    assert point.y is not None


def test_default_constructor_should_create_zero_object():
    point = Point()

    assert point is not None
    assert point.x == 0
    assert point.y == 0


def test_filled_constructor_should_create_valid_object():
    random = Point.random()

    point = Point(x=random.x, y=random.y)

    assert point is not None
    assert point.x == random.x
    assert point.y == random.y
