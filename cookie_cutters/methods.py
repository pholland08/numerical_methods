

def bisect(fn: callable, bounds: (float, float), tolerance: float) -> float:
    """
    :param fn:
    :param bounds: Tuple for lower bound, upper bound
    :param tolerance:
    :return: float
    """
    lower_bound = min(bounds) if min(bounds) != 0 else tolerance/2
    upper_bound = max(bounds) if max(bounds) != 0 else -tolerance/2

    lower_result = float(fn(lower_bound))
    upper_result = float(fn(upper_bound))

    if abs(lower_result) < abs(tolerance):
        return lower_bound

    elif abs(upper_result) < abs(tolerance):
        return upper_bound

    elif lower_result * upper_result < 0:
        mid_point = (lower_bound + upper_bound)/2
        mid_result = float(fn(mid_point))

        if abs(mid_result) < abs(tolerance):
            return mid_point

        elif mid_result * lower_result < 0:
            return bisect(fn, (lower_bound, mid_point), tolerance)

        elif mid_result * upper_result < 0:
            return bisect(fn, (mid_point, upper_bound), tolerance)

    raise Exception("Root not found")


def newton_raphson(fn: callable, dfn: callable, x_initial: float, max_iterations: int) -> float:
    """
    :param fn: Original function
    :param dfn: Derivative of original function
    :param x_initial: Non-zero starting point
    :param max_iterations:
    :return:
    """
    if max_iterations > 0:
        fx = x_initial - (fn(x_initial) / dfn(x_initial))
        return newton_raphson(fn, dfn, fx, max_iterations-1)

    else:
        return x_initial


if __name__ == '__main__':
    print(bisect(lambda x: x**3, (-1, 1), .00001))
    print(newton_raphson(lambda x: x**3 - 20, lambda x: 3*(x**2), 3, 3))
