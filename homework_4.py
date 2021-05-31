import numpy as np
import matplotlib.pyplot as plt
from runge_kutta_4 import *
from Kuramoto import *

N = 50
Nt = 1500
dt = 0.001

#adjacency matrix
K = 50*(np.ones((N, N)) - np.eye(N))

def randomTheta(N):
    return(np.random.random(N)*2*np.pi)

def randomOmega(N):
    return(np.random.standard_cauchy(N)*2*np.pi)

def f(K, omega, theta):
    N = len(theta)
    func=[]
    betrag, phase = order_parameter(theta)
    for i in range(0,N):
        func.append(omega[i]+K*betrag*np.sin(phase-theta[i]))
    return np.array(func)



circle = np.linspace(0,2*np.pi,256)
plt.plot(np.sin(circle), np.cos(circle), color="black")
plt.gca().set_aspect('equal')
plt.xlim(-1.5,1.5)
plt.title("Größeres Netzwerk")
plt.show()
