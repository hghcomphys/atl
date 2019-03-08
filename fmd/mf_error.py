"""
Handling errors
"""


def int_ge_zero(n):
    """
    Assertion exception for unexpected negative value of input argument.
    """
    int_n = int(n)
    if int_n < 0:
        raise ValueError  # ("Unexpected negative value for %s!" % int_ge_zero.__name__)
    else:
        return int_n


def float_ge_zero(x):
    """
    Assertion exception for unexpected negative value of float input argument.
    """
    float_x = float(x)
    if float_x < 0.0:
        raise ValueError  # Exception("Unexpected negative value for %s!" % float_ge_zero.__name__)
    else:
        return float_x
