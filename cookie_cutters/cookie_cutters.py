import math
import methods

fn_a = {
    "fn" : lambda x: (1/x)-5,
    "fn_str" : "(1/x)-5",
    "dfn1": lambda x: -1/(x**2),
    "dfn2": lambda x: 2/(x**3),
    "bounds": (0.0, 0.25),
    "root": 0.2
}

fn_b = {
    "fn" : lambda x: math.e**x - 2,
    "fn_str" : "e^x - 2",
    "dfn1": lambda x: math.e**x,
    "dfn2": lambda x: math.e**x,
    "bounds": (0.0, 1.0),
    "root": 0.69314718
}

fn_c = {
    "fn" : lambda x: x**3 - 2,
    "fn_str" : "x^3 - 2",
    "dfn1": lambda x: 3*x**2,
    "dfn2": lambda x: 6*x,
    "bounds": (0.0, 2.0),
    "root": 1.259921049
}

fn_d = {
    "fn" : lambda x: math.sin(x) - (x**2),
    "fn_str" : "sin(x) - (x^2)",
    "dfn1": lambda x: math.cos(x) - 2*x,
    "dfn2": lambda x: -math.sin(x) - 2,
    "bounds": (.25, 1.0),
    "root": 0.876726215
}

fn_e = {
    "fn" : lambda x: math.tan(x) - x,
    "fn_str" : "tan(x) - x",
    "dfn1": lambda x: 1/(math.cos(x)**2) - 1,
    "dfn2": lambda x: 2*math.tan(x)*(1/(math.cos(x)**2)),
    "bounds": (2.0, 4.5),
    "root": 4.49340946
}

fn_f = {
    "fn" : lambda x: x - (x**3) - 3,
    "fn_str" : "x - (x^3) - 3",
    "dfn1": lambda x: 1 - 3*(x**2),
    "dfn2": lambda x: -6*x,
    "bounds": (0.0, 2.0),
    "root": -1.671699881
}


def get_bisection_iterations(thing, tolerance):
    try:
        return methods.bisect(thing["fn"], thing['bounds'], tolerance)['iterations']

    except:
        return "Fail"


def get_newton_iterations(thing, tolerance):
    try:
        return methods.newton_raphson(thing["fn"], thing["dfn1"], thing['bounds'][1], tolerance)['iterations']

    except:
        return "Fail"


def get_secant_iterations(thing, tolerance):
    try:
        return methods.secant(thing['fn'], thing['bounds'][0], thing['bounds'][1], tolerance)['iterations']

    except:
        return "Fail"


def get_modified_newton_iterations(thing, tolerance):
    try:
        return methods.modified_newton(thing["fn"], thing["dfn1"], thing['dfn2'], thing['bounds'][1], tolerance)['iterations']

    except:
        return "Fail"


def compare_all():
    things = [fn_a,
              fn_b,
              fn_c,
              fn_d,
              fn_e,
              fn_f]
    tolerance = 10**-8

    print(*["fn".ljust(20), "root".ljust(15), "Bisect".ljust(10), "NewtonR".ljust(10), "Secant".ljust(10), "Modified NewtonR"], sep="\t")
    for thing in things:
        bisection_iterations = get_bisection_iterations(thing, tolerance)
        nr_iterations = get_newton_iterations(thing, tolerance)
        secant_iterations = get_secant_iterations(thing, tolerance)
        modified_newton_iterations = get_modified_newton_iterations(thing, tolerance)
        print(*[thing['fn_str'].ljust(20), str(thing['root']).ljust(15), str(bisection_iterations).ljust(10), str(nr_iterations).ljust(10), str(secant_iterations).ljust(10), modified_newton_iterations], sep="\t")


if __name__ == '__main__':
    compare_all()
