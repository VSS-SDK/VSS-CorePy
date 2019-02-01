from vsscorepy.domain.ball import Ball


def test_rand_should_create_an_valid_object():
    ball = Ball.random()

    assert ball is not None
    assert ball.x is not None
    assert ball.y is not None
    assert ball.speed_x is not None
    assert ball.speed_y is not None


def test_default_constructor_should_create_zero_object():
    ball = Ball()

    assert ball is not None
    assert ball.x == 0
    assert ball.y == 0
    assert ball.speed_x == 0
    assert ball.speed_y == 0


def test_filled_constructor_should_create_valid_object():
    random = Ball.random()

    point = Ball(x=random.x, y=random.y, speed_x=random.speed_x, speed_y=random.speed_y)

    assert point is not None
    assert point.x == random.x
    assert point.y == random.y
    assert point.speed_x == random.speed_x
    assert point.speed_y == random.speed_y
