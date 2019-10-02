import math
import sys


def bisect(fn: callable,
           bounds: (float, float),
           tolerance: float,
           current_iteration: float = 0,
           max_iterations: float = 0) -> dict:
    """
    :param fn:
    :param bounds: Tuple for lower bound, upper bound
    :param tolerance:
    :param current_iteration:
    :param max_iterations:
    :return: {root: float, iterations: int, max_iterations: int, error: float}
    """

    lower_bound = min(bounds) if min(bounds) != 0 else sys.float_info.min
    upper_bound = max(bounds) if max(bounds) != 0 else -sys.float_info.min

    lower_result = float(fn(lower_bound))
    upper_result = float(fn(upper_bound))
    current_iteration = current_iteration + 1

    if max_iterations == 0:
        max_iterations = calculate_bisection_iterations(bounds, tolerance)

    if abs(lower_result) <= abs(tolerance):
        return {"root": lower_bound,
                "iterations": current_iteration,
                "max_iterations": max_iterations,
                "error": 0}

    elif abs(upper_result) <= abs(tolerance):
        return {"root": upper_bound,
                "iterations": current_iteration,
                "max_iterations": max_iterations,
                "error": 0}

    elif signs_differ(lower_result, upper_result):
        mid_point = (lower_bound + upper_bound)/2
        mid_result = fn(mid_point)

        if abs(mid_result) < abs(tolerance):
            return {"root": mid_point,
                    "iterations": current_iteration + 1,
                    "max_iterations": max_iterations,
                    "error": 0}

        elif signs_differ(mid_result, lower_result):
            result = bisect(fn, (lower_bound, mid_point), tolerance, current_iteration, max_iterations)
            if result["error"] == 0:
                result["error"] = calculate_relative_difference(result["root"], lower_bound)
            return result

        elif signs_differ(mid_result, upper_result):
            result = bisect(fn, (mid_point, upper_bound), tolerance, current_iteration, max_iterations)
            if result["error"] == 0:
                result["error"] = calculate_relative_difference(result["root"], upper_bound)
            return result

    raise Exception("Root not found")


def signs_differ(n1: float, n2: float):
    return n1 * n2 < 0


def calculate_bisection_iterations(bounds: tuple, tolerance: float) -> int:
    """
    ceil(nlog(upper-lower)-nlog(tolerance)/log2)+1
    :param bounds:
    :param tolerance:
    :return:
    """
    return math.ceil(math.log(abs(max(bounds)-min(bounds))/tolerance, 2) - 1)


def calculate_relative_difference(current_value: float, previous_value: float) -> float:
    return abs((current_value - previous_value)/current_value) * 100


def newton_raphson(fn: callable, dfn: callable, x_0: float, tolerance: float) -> dict:
    """
    :param fn: Original function
    :param dfn: Derivative of original function
    :param x_0: Non-zero starting point
    :param tolerance:
    :return:
    """

    # todo: keep list of previous values to check for oscillation
    x_current = x_0 - (fn(x_0) / dfn(x_0))

    if calculate_relative_difference(x_current, x_0) > abs(tolerance):
        result = newton_raphson(fn, dfn, x_current, tolerance)
        result["iterations"] = result["iterations"] + 1
        return result

    else:
        return {"root": x_current,
                "iterations": 1}


def secant(fn: callable,
           x_0: float,
           x_1: float,
           tolerance: float) -> dict:
    """
    :param fn:
    :param x_0:
    :param x_1:
    :param tolerance:
    :return:
    """
    x_0 = tolerance if x_0 == 0 else x_0
    x_1 = tolerance if x_1 == 0 else x_1

    max_iterations = calculate_bisection_iterations((x_0, x_1), tolerance)
    x_current = x_1 - ((fn(x_1) * (x_1-x_0))/(fn(x_1) - fn(x_0)))

    if calculate_relative_difference(x_current, x_1) > tolerance:
        result = secant(fn, x_1, x_current, tolerance)
        result["iterations"] = result["iterations"] + 1
        result["max_iterations"] = max_iterations
        return result

    else:
        return {"root": x_current,
                "iterations": 1,
                "max_iterations": max_iterations}


def modified_newton(fn: callable, d1fn: callable, d2fn: callable, x_0: float, tolerance: float) -> dict:
    """
    :param fn:
    :param d1fn:
    :param d2fn:
    :param x_0:
    :param tolerance:
    :return:
    """

    #todo: Add oscillation detection
    x_current = x_0 - (fn(x_0)*d1fn(x_0))/((d1fn(x_0)**2) - fn(x_0)*d2fn(x_0))

    if abs(fn(x_current)) > abs(tolerance):
        result = modified_newton(fn, d1fn, d2fn, x_current, tolerance)
        result["iterations"] += 1
        return result

    else:
        return {"root": x_current,
                "iterations": 1}
