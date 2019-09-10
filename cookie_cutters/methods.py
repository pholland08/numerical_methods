import math


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
    :return: {root: float, iterations: int, max_iterations: int}
    """

    # todo: calculate precision -> ((new - old)/new)*100

    lower_bound = min(bounds) if min(bounds) != 0 else tolerance/2
    upper_bound = max(bounds) if max(bounds) != 0 else -tolerance/2

    lower_result = float(fn(lower_bound))
    upper_result = float(fn(upper_bound))
    current_iteration = current_iteration + 1

    if max_iterations == 0:
        max_iterations = calculate_bisection_iterations(bounds, tolerance)

    if abs(lower_result) < abs(tolerance):
        return {"root": lower_bound,
                "iterations": current_iteration,
                "max_iterations": max_iterations}

    elif abs(upper_result) < abs(tolerance):
        return {"root": upper_bound,
                "iterations": current_iteration,
                "max_iterations": max_iterations}

    elif lower_result * upper_result < 0:
        mid_point = (lower_bound + upper_bound)/2
        mid_result = fn(mid_point)

        if abs(mid_result) < abs(tolerance):
            return {"root": mid_point,
                    "iterations": current_iteration,
                    "max_iterations": max_iterations}

        elif signs_differ(mid_result, lower_result):
            return bisect(fn, (lower_bound, mid_point), tolerance, current_iteration, max_iterations)

        elif signs_differ(mid_result, upper_result):
            return bisect(fn, (mid_point, upper_bound), tolerance, current_iteration, max_iterations)

    raise Exception("Root not found")


def signs_differ(n1: float, n2: float):
    return n1 * n2 < 0


def calculate_bisection_iterations(bounds: tuple, tolerance: float) -> int:
    return math.ceil(math.log(abs(max(bounds)-min(bounds))/tolerance, 2))


def calculate_bisection_precision(current_value: float, previous_value: float) -> float:
    return abs((current_value - previous_value)/current_value) * 100


def newton_raphson(fn: callable, dfn: callable, x_initial: float, max_iterations: int) -> float:
    """
    :param fn: Original function
    :param dfn: Derivative of original function
    :param x_initial: Non-zero starting point
    :param max_iterations:
    :return:
    """

    # todo: calculate precision
    # todo: keep list of previous values to check for oscillation

    if max_iterations > 0:
        fx = x_initial - (fn(x_initial) / dfn(x_initial))
        return newton_raphson(fn, dfn, fx, max_iterations-1)

    else:
        return x_initial


def secant(fn: callable, x: float) -> float:
    pass
