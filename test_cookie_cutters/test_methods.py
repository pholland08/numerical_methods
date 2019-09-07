from unittest import TestCase
from cookie_cutters import methods
import math

"""
· fn a:  5=1/x, x_0=0.25
· fn b:  2=e^x, x_0=1
· fn c:  2=x^3, x_0=2
· fn d:  x^2=sin(x), x_0=1
· fn e:  x=tan(x), x_0=4.5
· fn f:  x-x^3=3, x_0=2
"""

tolerance = 10 ** -3


class TestBisection(TestCase):

    def test_returns_within_bounds(self):
        lower_bound = -1
        upper_bound = 1
        result = methods.bisect(lambda x: (x**3), (lower_bound, upper_bound), tolerance)
        self.assertTrue(lower_bound < result < upper_bound)

    def test_returns_within_tolerance(self):
        result = methods.bisect(lambda x: (x**3 - 20), (-1, 4), tolerance)
        self.assertTrue(2.7144 - tolerance < result < 2.7144 + tolerance)

    def test_midpoint_root_succeeds(self):
        result = methods.bisect(lambda x: x**3, (-1, 1), tolerance)
        self.assertTrue(-tolerance < result < tolerance)

    def test_fn_a(self):
        result = methods.bisect(lambda x: (1/x) - 5, (0, .25), tolerance)
        self.assertTrue(.2 - tolerance < result < .2 + tolerance)

    def test_fn_b(self):
        result = methods.bisect(lambda x: math.e**x - 2, (0, 1), tolerance)
        self.assertTrue(.69315 - tolerance < result < .69315 + tolerance)

    def test_fn_c(self):
        result = methods.bisect(lambda x: x**3 - 2, (0, 2), tolerance)
        self.assertTrue(1.2599 - tolerance < result < 1.2599 + tolerance)

    def test_fn_d(self):
        result = methods.bisect(lambda x: math.sin(x) - (x**2), (0, 1), tolerance)
        self.assertTrue(.8767125 - tolerance < result < .8767125 + tolerance)

    def test_fn_e(self):
        result = methods.bisect(lambda x: math.tan(x) - x, (1, 4.5), tolerance)
        self.assertTrue(4.4935 - tolerance < result < 4.4935 + tolerance)

    def test_fn_f(self):
        result = methods.bisect(lambda x: x - (x**3) - 3, (0, -2), tolerance)
        self.assertTrue(-1.6717 - tolerance < result < -1.6717 + tolerance)


class TestNewtonRaphson(TestCase):
    """
    todo: find a reliable way to test this...
    """

    def test_specific_parameters(self):
        result = methods.newton_raphson(lambda x: x**3 - 20, lambda x: 3*(x**2), 3, 10)
        self.assertAlmostEqual(result, 2.714, 3)

    def test_fn_a(self):
        result = methods.newton_raphson(lambda x: (1/x) - 5, lambda x: -1/(x**2), .25, 10)
        self.assertTrue(.2 - tolerance < result < .2 + tolerance)

    def test_fn_b(self):
        result = methods.newton_raphson(lambda x: math.e**x - 2, lambda x: math.e**x, 1, 10)
        self.assertTrue(.69315 - tolerance < result < .69315 + tolerance)

    def test_fn_c(self):
        result = methods.newton_raphson(lambda x: x**3 - 2, lambda x: 3*x**2, 2, 10)
        self.assertTrue(1.2599 - tolerance < result < 1.2599 + tolerance)

    def test_fn_d(self):
        result = methods.newton_raphson(lambda x: math.sin(x) - (x**2), lambda x: math.cos(x) - 2*x, 1, 10)
        self.assertTrue(.8767125 - tolerance < result < .8767125 + tolerance)

    def test_fn_e(self):
        result = methods.newton_raphson(lambda x: math.tan(x) - x, lambda x: 1/(math.cos(x)**2) - 1, 4.5, 10)
        self.assertTrue(4.4935 - tolerance < result < 4.4935 + tolerance)

    def test_fn_f(self):
        result = methods.newton_raphson(lambda x: x - (x**3) - 3, lambda x: 1 - 3*(x**2), -2, 10)
        self.assertTrue(-1.6717 - tolerance < result < -1.6717 + tolerance)
