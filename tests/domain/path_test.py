from vsscorepy.domain.path import Path


def test_rand_should_create_an_valid_object():
    path = Path.random()

    assert path is not None
    assert path.points is not None
    assert len(path.points) > 0

    for point in path.points:
        assert point is not None


def test_default_constructor_should_create_zero_object():
    path = Path()

    assert path is not None
    assert path.points is not None
    assert len(path.points) == 0


def test_filled_constructor_should_create_valid_object():
    random = Path.random()

    path = Path(points=random.points)

    assert path is not None
    assert path.points is not None
    assert len(path.points) == len(random.points)

    zip_points = zip(path.points, random.points)

    for zip_point in zip_points:
        assert zip_point[0] == zip_point[1]


def test_clean_should_works_properly():
    path = Path.random()
    path.clean()

    assert path is not None
    assert path.points is not None
    assert len(path.points) == 0
