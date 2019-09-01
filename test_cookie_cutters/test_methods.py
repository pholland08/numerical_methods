from unittest import TestCase
from cookie_cutters import methods


class TestBisection(TestCase):
    def test_returns_within_bounds(self):
        lower_bound = -1
        upper_bound = 1
        result = methods.bisect(lambda x: (x**3), (lower_bound, upper_bound), 0.0001)
        self.assertGreaterEqual(result, lower_bound)
        self.assertLessEqual(result, upper_bound)

    def test_returns_within_tolerance(self):
        tolerance = .0001
        result = methods.bisect(lambda x: (x**3 - 20), (-1, 4), tolerance)
        self.assertGreaterEqual(result, 2.7144 - tolerance)
        self.assertLessEqual(result, 2.7144 + tolerance)

    def test_midpoint_root_succeeds(self):
        result = methods.bisect(lambda x: x**3, (-1, 1), .0001)
        self.assertAlmostEqual(result, 0)


class TestNewtonRaphson(TestCase):
    """
    todo: find a reliable way to test this...
    """

    def test_specific_parameters(self):
        result = methods.newton_raphson(lambda x: x**3 - 20, lambda x: 3*(x**2), 3, 3)
        self.assertAlmostEqual(result, 2.714, 3)
