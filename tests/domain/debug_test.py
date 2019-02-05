from vsscorepy.domain.debug import Debug


def test_rand_should_create_an_valid_object():
    debug = Debug.random()

    assert debug is not None

    assert debug.step_points is not None
    assert len(debug.step_points) > 0

    for step_point in debug.step_points:
        assert step_point is not None

    assert debug.final_poses is not None
    assert len(debug.final_poses) > 0

    for final_pose in debug.final_poses:
        assert final_pose is not None

    assert debug.paths is not None
    assert len(debug.paths) > 0

    for path in debug.paths:
        assert path is not None


def test_default_constructor_should_create_zero_object():
    debug = Debug()

    assert debug is not None
    assert debug.step_points is not None
    assert len(debug.step_points) == 0
    assert debug.final_poses is not None
    assert len(debug.final_poses) == 0
    assert debug.paths is not None
    assert len(debug.paths) == 0


def test_filled_constructor_should_create_valid_object():
    random = Debug.random()

    debug = Debug(step_points=random.step_points, final_poses=random.final_poses, paths=random.paths)

    assert debug is not None

    assert debug.step_points is not None
    assert len(debug.step_points) == len(random.step_points)

    zip_step_points = zip(debug.step_points, random.step_points)

    for zip_step_point in zip_step_points:
        assert zip_step_point[0] == zip_step_point[1]

    assert debug.final_poses is not None
    assert len(debug.final_poses) == len(random.final_poses)

    zip_final_poses = zip(debug.final_poses, random.final_poses)

    for zip_final_pose in zip_final_poses:
        assert zip_final_pose[0] == zip_final_pose[1]

    assert debug.paths is not None
    assert len(debug.paths) == len(random.paths)

    zip_paths = zip(debug.paths, random.paths)

    for zip_path in zip_paths:
        assert zip_path[0] == zip_path[1]


def test_clean_should_works_properly():
    debug = Debug.random()
    debug.clean()

    assert debug is not None
    assert debug.step_points is not None
    assert len(debug.step_points) == 0
    assert debug.final_poses is not None
    assert len(debug.final_poses) == 0
    assert debug.paths is not None
    assert len(debug.paths) == 0
