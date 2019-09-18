import math
from unittest import TestCase
from cookie_cutters import methods

tolerance = 10 ** -8


class TestSecant(TestCase):
    def test_secant_root_within_tolerance(self):
        result = methods.secant(lambda x: x**3 - 20, 4, 5.5, tolerance)
        self.assertTrue(2.71441761 - tolerance <= result["root"] <= 2.71441761 + tolerance)

    def test_fn_a(self):
        """
        5=1/x, x_0=0.25
        """

        result = methods.secant(lambda x: (1/x) - 5, 0, .25, tolerance)
        self.assertTrue(.2 - tolerance <= result["root"] <= .2 + tolerance)

    def test_fn_b(self):
        """
        2=e^x, x_0=1
        """

        result = methods.secant(lambda x: math.e**x - 2, 0, 1, tolerance)
        self.assertTrue(0.69314718 - tolerance <= result["root"] <= 0.69314718 + tolerance)

    def test_fn_c(self):
        """
        2=x^3, x_0=2
        """

        result = methods.secant(lambda x: x**3 - 2, 0, 2, tolerance)
        self.assertTrue(1.259921049 - tolerance <= result["root"] <= 1.259921049 + tolerance)

    def test_fn_d(self):
        """
        x^2=sin(x), x_0=1
        """

        result = methods.secant(lambda x: math.sin(x) - (x**2), .25, 1, tolerance)
        self.assertTrue(0.876726215 - tolerance <= result["root"] <= 0.876726215 + tolerance)

    def test_fn_e(self):
        """
        x=tan(x), x_0=4.5
        """

        result = methods.secant(lambda x: math.tan(x) - x, 2, 4.5, tolerance)
        self.assertTrue(4.49340946 - tolerance <= result["root"] <= 4.49340946 + tolerance)

    def test_fn_f(self):
        """
        x-x^3=3, x_0=2
        """

        result = methods.secant(lambda x: x - (x**3) - 3, 0, 2, tolerance)
        self.assertTrue(-1.67169988 - tolerance <= result["root"] <= -1.67169988 + tolerance)



