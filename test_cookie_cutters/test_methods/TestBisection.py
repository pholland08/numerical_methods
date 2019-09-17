from cookie_cutters import methods
from unittest import TestCase
import math

tolerance = 10 ** -8


class TestBisection(TestCase):

    def test_bisection_precision(self):
        result = methods.bisect(lambda x: (x**3 - 20), (-1, 4), tolerance)
        print(result)

    def test_calculate_bisection_error(self):
        precision = methods.calculate_bisection_error(3.25, 2.5)
        self.assertAlmostEqual(23.0769, precision, 4)

    def test_calculate_bisection_iterations(self):
        result = methods.calculate_bisection_iterations((0, 1), .001)
        self.assertEqual(9, result)

    def test_returns_within_bounds(self):
        lower_bound = -1
        upper_bound = 1
        result = methods.bisect(lambda x: (x**3), (lower_bound, upper_bound), tolerance)
        self.assertTrue(lower_bound <= result["root"] <= upper_bound)

    def test_returns_within_tolerance(self):
        result = methods.bisect(lambda x: (x**3 - 20), (-1, 4), tolerance)
        self.assertTrue(2.71441762 - tolerance <= result["root"] <= 2.71441762 + tolerance)

    def test_midpoint_root_succeeds(self):
        result = methods.bisect(lambda x: x**3, (-1, 1), tolerance)
        print(result)
        self.assertTrue(-tolerance <= result["root"] <= tolerance)

    def test_expected_iterations(self):
        result = methods.bisect(lambda x: x**3, (-1, 5), tolerance)
        self.assertGreaterEqual(result["max_iterations"], result["iterations"])

    def test_max_iterations(self):
        fn = lambda x: x**3 - 20
        bounds = (0, 5)
        result = methods.bisect(fn, bounds, tolerance)
        print(result)
        self.assertGreaterEqual(result["max_iterations"], methods.calculate_bisection_iterations(bounds, tolerance))

    def test_fn_a(self):
        """
        5=1/x, x_0=0.25
        """

        result = methods.bisect(lambda x: (1/x) - 5, (0, .25), tolerance)
        self.assertTrue(.2 - tolerance <= result["root"] <= .2 + tolerance)

    def test_fn_b(self):
        """
        2=e^x, x_0=1
        """

        result = methods.bisect(lambda x: math.e**x - 2, (0, 1), tolerance)
        self.assertTrue(0.69314718 - tolerance <= result["root"] <= 0.69314718 + tolerance)

    def test_fn_c(self):
        """
        2=x^3, x_0=2
        """

        result = methods.bisect(lambda x: x**3 - 2, (0, 2), tolerance)
        self.assertTrue(1.259921049 - tolerance <= result["root"] <= 1.259921049 + tolerance)

    def test_fn_d(self):
        """
        x^2=sin(x), x_0=1
        """

        result = methods.bisect(lambda x: math.sin(x) - (x**2), (.25, 1), tolerance)
        self.assertTrue(0.876726215 - tolerance <= result["root"] <= 0.876726215 + tolerance)

    def test_fn_e(self):
        """
        x=tan(x), x_0=4.5
        """

        result = methods.bisect(lambda x: math.tan(x) - x, (2, 4.5), tolerance)
        self.assertTrue(4.49340946 - tolerance <= result["root"] <= 4.49340946 + tolerance)

    def test_fn_f(self):
        """
        x-x^3=3, x_0=2
        """

        with self.assertRaises(Exception) as context:
            result = methods.bisect(lambda x: x - (x**3) - 3, (0, 2), tolerance)

        self.assertTrue("Root not found" in str(context.exception))
