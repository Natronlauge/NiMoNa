import numpy as np

def rk4_step(rhs, x, function_parameters, h):
    k1 = rhs(x, *function_parameters)
    k2 = rhs(x + k1*h/2., *function_parameters)
    k3 = rhs(x + k2*h/2., *function_parameters)
    k4 = rhs(x + k3*h, *function_parameters)
    theta = x+ h/6.*(k1+ 2*(k2+k3) + k4)
    return theta