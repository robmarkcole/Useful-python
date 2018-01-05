"""
This module provides the RandomGen class with method next_num() for generating
random numbers with a predefined probability.
"""
import numpy as np
import math


class RandomGen(object):
    """
    Class to randomly draw from a probability distribution. Probabilities
    are normalised to ensure they sum to unity.
    """
    def __init__(self, random_nums, probabilities):
        if len(random_nums) != len(probabilities):
            raise ValueError(
                'random_nums and probabilities must be equal length.')

        if math.fsum(probabilities) != 1.0:
            raise ValueError(
                'Your probabilities do not sum to 1.0.')

        self._random_nums = random_nums
        self._probabilities = probabilities
        self._cumsum = [sum(
            self._probabilities[:i+1]) for i, v in enumerate(
            self._probabilities)]

    def next_num(self):
        """
        Generate a single random number.
        """
        rand = np.random.random()
        index_greater_than_rand = [i for i, v in enumerate(
            self._cumsum) if v > rand][0]
        return self._random_nums[index_greater_than_rand]
