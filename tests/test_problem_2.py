import numpy as np
from problem2.solutions import sum_image_channels


def test_fixture_images(uses_loop, image_fixture):
    assert not uses_loop(sum_image_channels)
    path, expected = image_fixture
    actual = sum_image_channels(path)
    np.testing.assert_allclose(actual, expected)
