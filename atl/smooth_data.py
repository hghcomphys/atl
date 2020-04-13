"""
Smooth a given input data
"""
import numpy as np


def smooth_data(x=[], y=[], n_ave=1, step=1):
    """
    This function takes x,y as input array data and return smoothed data
    by averaging over the given number of neighbours and step.

    Example:

    x  = np.linspace(0,10,100)
    y  = np.sin(x)+2*(np.random.rand(len(x))-0.5)
    xs,ys = smooth_data(x,y,5,2)

    """

    N = len(y); sx = []; sy = []
    for i in range(0, N, step):

        sx.append(x[i])

        if (i + 1) < n_ave:
            sy.append(np.mean(y[0:2 * i + 1:1]))

        elif (N - i) < n_ave:
            sy.append(np.mean(y[2 * i - N + 1:N]))

        else:
            sy.append(np.mean(y[i - n_ave + 1:i + n_ave:1]))

    return sx, sy