import numpy as np
import matplotlib.pyplot as plt

#Parameter der Aufgabenstellung
epsilon1 = 2.0 #Fortpflanzungsrate Hasen
epsilon2 = 0.8 #Sterberate Füchse
gamma1 = 0.02 #Sterberate Hasen durch Füchse
gamma2 = 0.002 #Fortpflanzungsrate Füchse durch genug Futter - Ich hab einen anderen Parameter gewählt
h = 0.025 #Schrittweite Euler
p_rabbit = 100 #Random gewählte Hasen-Startpopulation
p_fox = 80 #Random gewählte Fuchs-Startpopulation

#Euler-Methode
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
plt.title('Population gegen die Zeit mit Euler-Methode')
plt.legend()
plt.xlabel('$t$')
plt.ylabel('$p(t)$')
plt.show()
plt.plot(p_euler, p_fuuux, color='red')
plt.title('Phasenraumtrajektorie mit der Euler-Methode')
plt.xlabel('$Hasenpopulation$')
plt.ylabel('$Fuchspopulation$')
plt.show()

#Heun-Methode

t_heun = np.arange(0, 50, h)
p1_heun = np.arange(0, 50, h)
p2_heun = np.arange(0, 50, h)
p1_heun[0] = p_rabbit
p2_heun[0] = p_fox

i = 1
while i < round(t_heun.size):
    p1_heun[i] = p1_heun[round(i-1)]+h*(p1_heun[round(i-1)]*(epsilon1-(gamma1*p2_heun[round(i-1)])))
    p2_heun[i] = p2_heun[round(i-1)]+h*(-p2_heun[round(i-1)]*(epsilon2-(gamma2*p1_heun[round(i-1)])))
    p1_heun[i] = p1_heun[round(i-1)]+h*0.5*((p1_heun[round(i-1)]*(epsilon1-(gamma1*p2_heun[round(i-1)])))+p1_heun[round(i)]*(epsilon1-gamma1*p2_heun[round(i)]))
    p2_heun[i] = p2_heun[round(i-1)]+h*0.5*((-p2_heun[round(i-1)]*(epsilon2-(gamma2*p1_heun[round(i-1)])))-p2_heun[round(i)]*(epsilon2-gamma2*p1_heun[round(i)]))
    i = i+1

plt.plot(t_heun, p1_heun, color='blue', label='Hasenpopulation')
plt.plot(t_heun, p2_heun, color='red', label='Fuchspopulation')
plt.title('Populationen gegen die Zeit mit der Heun-Methode')
plt.legend()
plt.xlabel('$t$')
plt.ylabel('$p(t)$')
plt.show()
plt.title('Phasenraumtrajektorie mit der Heun-Methode')
plt.xlabel('$Hasenpopulation$')
plt.ylabel('$Fuchspopulation$')
plt.plot(p1_heun, p2_heun, color='red')
plt.show()

#Vergleich

plt.plot(p_euler,p_fuuux, color='red', label ='Euler-Methode')
plt.plot(p1_heun, p2_heun, color='blue', label='Heun-Methode')
plt.title('Phasenraumtrajektorie mit Euler- und Heun-Methode im Vergleich')
plt.legend()
plt.xlabel('$Hasenpopulation$')
plt.ylabel('$Fuchspopulation$')
plt.show()
