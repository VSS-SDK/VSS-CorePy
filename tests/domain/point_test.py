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


def test_eq_should_be_true_if_all_parameters_are_equal():
    point1 = Point.random()
    point2 = Point(x=point1.x, y=point1.y)

    assert point1 == point2

    point2.x = point2.x + 1

    assert point1 != point2

    point2.x = point2.x - 1
    point2.y = point2.y + 1

    assert point1 != point2

