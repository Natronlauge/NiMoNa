import numpy as np
import matplotlib.pyplot as plt

#analytisch für Aufgabenteil a

a = 1
h = 0.5
x0 = 0.5

x = np.linspace(0, 7, 256)
y = x0*np.exp(-a*x)

plt.plot(x,y)
plt.title('Aufgabenteil A')
plt.xlabel('$t$')
plt.ylabel('$x(t)$')

#numerisch für Teil a

i = h
n = i+h
x = np.linspace(0, h, 2)
y = np.linspace(0, h, 2)
y[0] = x0
y[1] = y[0]+(h*(-a*y[0]))
plt.plot (x, y, color='red')
while(n< 7+h):
    x = np.linspace(i, n, 2)
    y = y+(h*(-a*y))
    plt.plot(x, y, color='red')
    i = n
    n = n+h
    
plt.show()

#analytisch für Teil b

h = 0.1

x = np.linspace(0, 7, 256)
y = x0*np.exp(-a*x)

plt.plot(x,y)
plt.title('Aufgabenteil B')
plt.xlabel('$t$')
plt.ylabel('$x(t)$')

#numerisch für Teil b

i = h
n = i+h
x = np.linspace(0, h, 2)
y = np.linspace(0, h, 2)
y[0] = x0
y[1] = y[0]+(h*(-a*y[0]))
plt.plot (x, y, color='red')
while(n< 7+h):
    x = np.linspace(i, n, 2)
    y = y+(h*(-a*y))
    plt.plot(x, y, color='red')
    i = n
    n = n+h
    
plt.show()
    
#analytisch für Teil c

h = 0.01

x = np.linspace(0, 7, 256)
y = x0*np.exp(-a*x)

plt.plot(x,y)
plt.title('Aufgabenteil C')
plt.xlabel('$t$')
plt.ylabel('$x(t)$')

#numerisch für Teil c

i = h
n = i+h
x = np.linspace(0, h, 2)
y = np.linspace(0, h, 2)
y[0] = x0
y[1] = y[0]+(h*(-a*y[0]))
plt.plot (x, y, color='red')
while(n< 7+h):
    x = np.linspace(i, n, 2)
    y = y+(h*(-a*y))
    plt.plot(x, y, color='red')
    i = n
    n = n+h
    
plt.show()
    
#analytisch für teil d

a = 3
h = 0.5
x0 = 3

x = np.linspace(0, 7, 256)
y = x0*np.exp(-a*x)

plt.plot(x,y)
plt.title('Aufgabenteil D')
plt.xlabel('$t$')
plt.ylabel('$x(t)$')

#numerisch für teil d

i = h
n = i+h
x = np.linspace(0, h, 2)
y = np.linspace(0, h, 2)
y[0] = x0
y[1] = y[0]+(h*(-a*y[0]))
plt.plot (x, y, color='red')
while(n< 7+h):
    x = np.linspace(i, n, 2)
    y = y+(h*(-a*y))
    plt.plot(x, y, color='red')
    i = n
    n = n+h
    
plt.show()