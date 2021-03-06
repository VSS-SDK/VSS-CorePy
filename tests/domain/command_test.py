from vsscorepy.domain.command import Command


def test_rand_should_create_an_valid_object():
    command = Command.random()

    assert command is not None
    assert command.wheels_commands is not None
    assert len(command.wheels_commands) > 0

    for wheels_command in command.wheels_commands:
        assert wheels_command is not None


def test_default_constructor_should_create_zero_object():
    command = Command()

    assert command is not None
    assert command.wheels_commands is not None
    assert len(command.wheels_commands) == 0


def test_filled_constructor_should_create_valid_object():
    random = Command.random()

    command = Command(wheels_commands=random.wheels_commands)

    assert command is not None
    assert command.wheels_commands is not None
    assert len(command.wheels_commands) == len(random.wheels_commands)

    zip_wheels_commands = zip(command.wheels_commands, random.wheels_commands)

    for zip_wheels_command in zip_wheels_commands:
        assert zip_wheels_command[0] == zip_wheels_command[1]


def test_clean_should_works_properly():
    command = Command.random()
    command.clean()

    assert command is not None
    assert command.wheels_commands is not None
    assert len(command.wheels_commands) == 0
