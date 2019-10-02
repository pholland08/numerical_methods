from cookie_cutters import methods
from unittest import TestCase
import math

tolerance = 10**-8


class TestNewtonRaphson(TestCase):

    def test_specific_parameters(self):
        result = methods.newton_raphson(lambda x: x**3 - 20, lambda x: 3*(x**2), 3, tolerance)
        self.assertAlmostEqual(result["root"], 2.714, 3)

    def test_fn_a(self):
        """
        5=1/x, x_0=0.25
        """

        result = methods.newton_raphson(lambda x: (1/x) - 5, lambda x: -1/(x**2), .25, tolerance)
        self.assertTrue(.2 - tolerance < result["root"] < .2 + tolerance)

    def test_fn_b(self):
        """
        2=e^x, x_0=1
        """

        result = methods.newton_raphson(lambda x: math.e**x - 2, lambda x: math.e**x, 1, tolerance)
        self.assertTrue(0.69314718 - tolerance < result["root"] < 0.69314718 + tolerance)

    def test_fn_c(self):
        """
        2=x^3, x_0=2
        """

        result = methods.newton_raphson(lambda x: x**3 - 2, lambda x: 3*x**2, 2, tolerance)
        self.assertTrue(1.259921049 - tolerance < result["root"] < 1.259921049 + tolerance)

    def test_fn_d(self):
        """
        x^2=sin(x), x_0=1
        """

        result = methods.newton_raphson(lambda x: math.sin(x) - (x**2), lambda x: math.cos(x) - 2*x, 1, tolerance)
        self.assertTrue(0.876726215 - tolerance < result["root"] < 0.876726215 + tolerance)

    def test_fn_e(self):
        """
        x=tan(x), x_0=4.5
        """

        result = methods.newton_raphson(lambda x: math.tan(x) - x, lambda x: 1/(math.cos(x)**2) - 1, 4.5, tolerance)
        self.assertTrue(4.49340946 - tolerance < result["root"] < 4.49340946 + tolerance)

    def test_fn_f(self):
        """
        x-x^3=3, x_0=2
        """

        result = methods.newton_raphson(lambda x: x - (x**3) - 3, lambda x: 1 - 3*(x**2), 2, tolerance)
        self.assertTrue(-1.671699881 - tolerance < result["root"] < -1.671699881 + tolerance)
