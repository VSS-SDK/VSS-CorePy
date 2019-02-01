from vsscorepy.domain.state import State


def test_rand_should_create_an_valid_object():
    state = State.random()

    assert state is not None
    assert state.ball is not None
    assert state.team_blue is not None
    assert len(state.team_blue) > 0
    assert state.team_yellow is not None
    assert len(state.team_yellow) > 0


def test_default_constructor_should_create_zero_object():
    state = State()

    assert state is not None
    assert state.ball is not None
    assert state.team_blue is not None
    assert len(state.team_blue) == 0
    assert state.team_yellow is not None
    assert len(state.team_yellow) == 0


def test_filled_constructor_should_create_valid_object():
    random = State.random()

    state = State(ball=random.ball, team_blue=random.team_blue, team_yellow=random.team_yellow)

    assert state is not None
    assert len(state.team_blue) == len(random.team_blue)
    assert len(state.team_yellow) == len(random.team_yellow)


def test_clean_should_empty_wheels_commands():
    state = State.random()
    state.clean()

    assert state is not None
    assert state.ball is not None
    assert state.team_yellow is not None
    assert len(state.team_yellow) == 0
    assert state.team_blue is not None
    assert len(state.team_blue) == 0
