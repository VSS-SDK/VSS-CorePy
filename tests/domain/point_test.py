from vsscorepy.domain.point import Point

def test_default_constructor_should_create_zero_object():
    point = Point()

    assert point.x == 0
    assert point.y == 0