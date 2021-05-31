import numpy as np


def kuramoto(x, omegas, K):
    dx = np.zeros_like(x)
    for i in range(x.size):
        dx[i] = omegas[i] + np.dot(K[i, :], np.sin(x - x[i]))
    return dx


def kuramoto_loop(x, omegas, K):
    dx = np.zeros_like(x)
    for i in range(x.size):
        dx[i] = omegas[i]
        for j in range(x.size):
            dx[i] += K[i, j]*np.sin(x[j] - x[i])
    return dx

def order_parameter(theta):
    N = len(theta)
    im=0
    re=0
    for i in theta:
        im = im + np.sin(i)/N
        re = re + np.cos(i)/N
    return(np.sqrt(im**2+re**2), np.arccos(re))
