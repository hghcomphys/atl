"""
Handling errors
"""


def int_ge_zero(n):
    """
    Assertion error for unexpected negative value of input argument.
    """
    int_n = int(n)
    if int_n < 0:
        AssertionError("Unexpected negative value (int)!")
    else:
        return int_n


def float_ge_zero(x):
    """
    Assertion error for unexpected negative value of float input argument.
    """
    float_x = float(x)
    if float_x < 0.0:
        AssertionError("Unexpected negative value (float)!")
    else:
        return float_x
