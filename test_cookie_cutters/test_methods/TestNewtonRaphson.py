from cookie_cutters import methods
from unittest import TestCase
import math

tolerance = 10**-4


class TestNewtonRaphson(TestCase):

    def test_specific_parameters(self):
        result = methods.newton_raphson(lambda x: x**3 - 20, lambda x: 3*(x**2), 3, 10)
        self.assertAlmostEqual(result, 2.714, 3)

    def test_fn_a(self):
        """
        5=1/x, x_0=0.25
        """

        result = methods.newton_raphson(lambda x: (1/x) - 5, lambda x: -1/(x**2), .25, 10)
        self.assertTrue(.2 - tolerance < result < .2 + tolerance)

    def test_fn_b(self):
        """
        2=e^x, x_0=1
        """

        result = methods.newton_raphson(lambda x: math.e**x - 2, lambda x: math.e**x, 1, 10)
        self.assertTrue(.69315 - tolerance < result < .69315 + tolerance)

    def test_fn_c(self):
        """
        2=x^3, x_0=2
        """

        result = methods.newton_raphson(lambda x: x**3 - 2, lambda x: 3*x**2, 2, 10)
        self.assertTrue(1.2599 - tolerance < result < 1.2599 + tolerance)

    def test_fn_d(self):
        """
        x^2=sin(x), x_0=1
        """

        result = methods.newton_raphson(lambda x: math.sin(x) - (x**2), lambda x: math.cos(x) - 2*x, 1, 10)
        self.assertTrue(.8767125 - tolerance < result < .8767125 + tolerance)

    def test_fn_e(self):
        """
        x=tan(x), x_0=4.5
        """

        result = methods.newton_raphson(lambda x: math.tan(x) - x, lambda x: 1/(math.cos(x)**2) - 1, 4.5, 10)
        self.assertTrue(4.4935 - tolerance < result < 4.4935 + tolerance)

    def test_fn_f(self):
        """
        x-x^3=3, x_0=2
        """

        result = methods.newton_raphson(lambda x: x - (x**3) - 3, lambda x: 1 - 3*(x**2), -2, 10)
        self.assertTrue(-1.6717 - tolerance < result < -1.6717 + tolerance)
