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

    ball = Ball(x=random.x, y=random.y, speed_x=random.speed_x, speed_y=random.speed_y)

    assert ball is not None
    assert ball.x == random.x
    assert ball.y == random.y
    assert ball.speed_x == random.speed_x
    assert ball.speed_y == random.speed_y


def test_eq_should_be_true_if_all_parameters_are_equal():
    ball1 = Ball.random()
    ball2 = Ball(x=ball1.x, y=ball1.y, speed_x=ball1.speed_x, speed_y=ball1.speed_y)

    assert ball1 == ball2

    ball2.x = ball2.x + 1

    assert ball1 != ball2

    ball2.x = ball2.x - 1
    ball2.y = ball2.y + 1

    assert ball1 != ball2

    ball2.y = ball2.y - 1
    ball2.speed_x = ball2.speed_x + 1

    assert ball1 != ball2

    ball2.speed_x = ball2.speed_x - 1
    ball2.speed_y = ball2.speed_y + 1

    assert ball1 != ball2
