import numpy as np
from rc_random import RandomGen
import pytest

np.random.seed(1000)
random_nums = [-1, 0, 1, 2, 3]
probabilities = [0.01, 0.3, 0.58, 0.1, 0.01]


def test_class_init_failure():
    """
    Test that errors are raised correctly.
    """
    with pytest.raises(TypeError):
        RandomGen(1, [1, 2])

    with pytest.raises(ValueError):
        RandomGen([1], [1, 2])

    with pytest.raises(ValueError):
        RandomGen([1], [1.5])


def test_generator():
    """
    Test that the correct distribution is drawn.
    """
    g1 = RandomGen(random_nums, probabilities)
    assert g1.next_num() == 1

    test_draw = [g1.next_num() for i in range(1000000)]
    unique, counts = np.unique(test_draw, return_counts=True)
    expected_counts = [9942, 298499, 581460, 100093, 10006]
    np.testing.assert_array_equal(counts, expected_counts)
