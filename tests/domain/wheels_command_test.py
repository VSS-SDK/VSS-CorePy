from vsscorepy.domain.wheels_command import WheelsCommand


def test_rand_should_create_an_valid_object():
    wheels_command = WheelsCommand.random()

    assert wheels_command is not None
    assert wheels_command.left_vel is not None
    assert wheels_command.right_vel is not None


def test_default_constructor_should_create_zero_object():
    wheels_command = WheelsCommand()

    assert wheels_command is not None
    assert wheels_command.left_vel == 0
    assert wheels_command.right_vel == 0


def test_filled_constructor_should_create_valid_object():
    random = WheelsCommand.random()

    wheels_command = WheelsCommand(left_vel=random.left_vel, right_vel=random.right_vel)

    assert wheels_command is not None
    assert wheels_command.left_vel == random.left_vel
    assert wheels_command.right_vel == random.right_vel
