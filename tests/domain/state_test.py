from vsscorepy.domain.state import State


def test_rand_should_create_an_valid_object():
    state = State.random()

    assert state is not None
    assert state.ball is not None

    assert state.team_yellow is not None
    assert len(state.team_yellow) > 0

    for robot in state.team_yellow:
        assert robot is not None

    assert state.team_blue is not None
    assert len(state.team_blue) > 0

    for robot in state.team_blue:
        assert robot is not None


def test_default_constructor_should_create_zero_object():
    debug = State()

    assert debug is not None
    assert debug.ball is not None
    assert debug.team_yellow is not None
    assert len(debug.team_yellow) == 0
    assert debug.team_blue is not None
    assert len(debug.team_blue) == 0


def test_filled_constructor_should_create_valid_object():
    random = State.random()

    state = State(ball=random.ball, team_yellow=random.team_yellow, team_blue=random.team_blue)

    assert state is not None
    assert state.ball is not None

    assert state.team_blue is not None
    assert len(state.team_blue) == len(random.team_blue)

    zip_team_yellow = zip(state.team_blue, random.team_blue)

    for zip_robots in zip_team_yellow:
        assert zip_robots[0] == zip_robots[1]

    assert state.team_yellow is not None
    assert len(state.team_yellow) == len(random.team_yellow)

    zip_team_yellow = zip(state.team_yellow, random.team_yellow)

    for zip_robots in zip_team_yellow:
        assert zip_robots[0] == zip_robots[1]


def test_clean_should_works_properly():
    state = State.random()
    state.clean()

    assert state is not None
    assert state.ball is not None
    assert state.team_blue is not None
    assert len(state.team_blue) == 0
    assert state.team_yellow is not None
    assert len(state.team_yellow) == 0
