import numpy as np
import matplotlib.pyplot as plt

#Parameter der Aufgabenstellung
epsilon1 = 2.0 #Fortpflanzungsrate Hasen
epsilon2 = 0.8 #Sterberate Füchse
gamma1 = 0.02 #Sterberate Hasen durch Füchse
gamma2 = 0.002 #Fortpflanzungsrate Füchse durch genug Futter - Ich hab einen anderen Parameter gewählt, damit die Kurven schöner sind
h = 0.025 #Schrittweite Euler
p_rabbit = 35 #Random gewählte Hasen-Startpopulation
p_fox = 80 #Random gewählte Fuchs-Startpopulation
t_euler = np.arange(0, 50, h)
p_euler = np.arange(0, 50, h)
p_fuuux = np.arange(0, 50, h)
p_euler[0] = p_rabbit
p_fuuux[0] = p_fox

i = 1
while i < round(t_euler.size):
    p_euler[i] = p_euler[round(i-1)]+h*(p_euler[round(i-1)]*(epsilon1-(gamma1*p_fuuux[round(i-1)])))
    p_fuuux[i] = p_fuuux[round(i-1)]+h*(-p_fuuux[round(i-1)]*(epsilon2-(gamma2*p_euler[round(i-1)])))
    i = i+1

plt.plot(t_euler, p_euler, color='blue', label="Hasenpopulation")
plt.plot(t_euler, p_fuuux, color='red', label="Fuchspopulation")
plt.legend()
plt.xlabel('$t$')
plt.ylabel('$p(t)$')
plt.show()
plt.plot(p_euler, p_fuuux, color='red', label='Euler')
plt.legend()
plt.xlabel('$Hasenpopulation$')
plt.ylabel('$Fuchspopulation$')
plt.show()

