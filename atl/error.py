"""
Handling errors
"""


def int_ge_zero(n):
    """
    Assertion error for unexpected negative value of input argument.
    """
    int_n = int(n)
    if int_n < 0:
        AssertionError("Unexpected negative value!")
    else:
        return int_n