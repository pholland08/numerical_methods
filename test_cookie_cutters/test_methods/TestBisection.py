from cookie_cutters import methods
from unittest import TestCase
import math

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
        """
        5=1/x, x_0=0.25
        """

        result = methods.bisect(lambda x: (1/x) - 5, (0, .25), tolerance)
        self.assertTrue(.2 - tolerance < result < .2 + tolerance)

    def test_fn_b(self):
        """
        2=e^x, x_0=1
        """

        result = methods.bisect(lambda x: math.e**x - 2, (0, 1), tolerance)
        self.assertTrue(.69315 - tolerance < result < .69315 + tolerance)

    def test_fn_c(self):
        """
        2=x^3, x_0=2
        """

        result = methods.bisect(lambda x: x**3 - 2, (0, 2), tolerance)
        self.assertTrue(1.2599 - tolerance < result < 1.2599 + tolerance)

    def test_fn_d(self):
        """
        x^2=sin(x), x_0=1
        """

        result = methods.bisect(lambda x: math.sin(x) - (x**2), (0, 1), tolerance)
        self.assertTrue(.8767125 - tolerance < result < .8767125 + tolerance)

    def test_fn_e(self):
        """
        x=tan(x), x_0=4.5
        """

        result = methods.bisect(lambda x: math.tan(x) - x, (1, 4.5), tolerance)
        self.assertTrue(4.4935 - tolerance < result < 4.4935 + tolerance)

    def test_fn_f(self):
        """
        x-x^3=3, x_0=2
        """

        with self.assertRaises(Exception) as context:
            result = methods.bisect(lambda x: x - (x**3) - 3, (0, 2), tolerance)

        self.assertTrue("Root not found" in str(context.exception))
