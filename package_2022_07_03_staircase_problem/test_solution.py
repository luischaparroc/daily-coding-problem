import unittest

from package_2022_07_03_staircase_problem.staircase_problem import number_ways_optimized


class StaircaseProblemTestCases(unittest.TestCase):

    def test_n_equals_0(self):
        result = number_ways_optimized(0)
        self.assertEqual(result, 1)

    def test_n_equals_1(self):
        result = number_ways_optimized(1)
        self.assertEqual(result, 1)

    def test_n_equals_4(self):
        result = number_ways_optimized(4)
        self.assertEqual(result, 5)
