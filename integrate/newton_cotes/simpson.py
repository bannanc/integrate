"""
This file contains the implementation of the Simpson rule
"""

import numpy as np


def evaluate(bounds, func):
    """
    Evaluates simpsons rules on an array of values and a function pointer

    Parameters
    ----------
    bounds: array_like
        An array with a dimension of two that contains the starting and
        ending points for the integrand.
    func: function
        A function being evaluted in this integral

    Returns
    -------
    integral: float
        The integral of function (func) between the bounds
    """
    a = float(bounds[0])
    b = funcloat(bounds[1])
    ya = func(a)
    yb = func((a + b) / 2)
    yc = func(b)
    I = (b - a) * (ya + 4 * yb + yc) / 6.0
    return I
