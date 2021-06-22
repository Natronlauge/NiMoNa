import numpy as np
import matplotlib.pyplot as plt

def kuramoto(x, omegas, K):
    # print(x.shape)
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

def order_parameter(x):
    real = np.mean(np.cos(x))
    imag = np.mean(np.sin(x))
    r = np.sqrt(real**2 + imag**2)
    psi = np.angle(real + 1j*imag)
    return r, psi

def plot_network(ax, pos, A, C, thetas, Ausfall):
    ax.clear()
    ax.scatter(pos[:, 0], pos[:, 1], c=thetas%(2*np.pi), cmap='hsv', vmin=0, vmax=2*np.pi)
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if A[i, j] != 0:
                ax.plot(pos[[i,j], 0], pos[[i,j], 1], 'k-', zorder=0)
            if (Ausfall==1):
                if C[i, j] > 1:
                    ax.plot(pos[[i,j], 0], pos[[i, j], 1], 'r', zorder=0)
                if C[i, j] < -1:
                    ax.plot(pos[[i,j], 0], pos[[i, j], 1], 'g', zorder=0)

    ax.set_aspect('equal')
    # remove ticks
    ax.set_xticks([])
    ax.set_yticks([])
    return ax

