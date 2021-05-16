import numpy as np
import matplotlib.pyplot as plt

#Ich hab es so versucht wie Lennart, weil ich es noch nicht so richtig verstanden hab

#Kupplungskonstante
k = 50

#Aufgabenstellung und was Lennart mir gesagt hat, weil ich es nicht verstanden habe.
phase1_start = 0.5
phase2_start = 1
phase3_start = 1.5
omega1 = 0.19
omega2 = 0.2
omega3 = 0.21

phase_i = [phase1_start, phase2_start, phase3_start]

h = 0.001
t_end = 40
t = np.arange(0, t_end, h)

phase1 = np.arange(0, t_end, h)
phase1[0] = phase1_start
phase2 = np.arange(0, t_end, h)
phase2[0] = phase2_start
phase3 = np.arange(0, t_end, h)
phase3[0] = phase3_start

#adjacency matrix K:
K = [[0, k, k], [k, 0, k], [k, k, 0]]

for n in range(t.size-1):
    k1 = [omega1, omega2, omega3]
    for i in range(3):
        for j in range(3):
            k1[i] = k1[i]+K[i][j]*np.sin(phase_i[j]-phase_i[i])

    k2 = [omega1, omega2, omega3]
    for i in range(3):
        for j in range(3):
            k2[i] = k2[i]+K[i][j]*np.sin((phase_i[j]+(h/2))-(phase_i[i]+(h/2)*k1[i]))

    k3 = [omega1, omega2, omega3]
    for i in range(3):
        for j in range(3):
            k3[i] = k3[i]+K[i][j]*np.sin((phase_i[j]+(h/2))-(phase_i[i]+(h/2)*k2[i]))

    k4 = [omega1, omega2, omega3]
    for i in range(3):
        for j in range(3):
            k4[i] =k4[i]+K[i][j]*np.sin((phase_i[j]+h)-(phase_i[i]+h*k3[i]))

    for i in range(3):
        phase_i[i] = phase_i[i]+(h/6)*(k1[i]+k2[i]+k3[i]+k4[i])
    phase1[n+1] = phase_i[0]
    phase2[n+1] = phase_i[1]
    phase3[n+1] = phase_i[2]

plt.plot(t, phase1, color="red", label="Phase 1")
plt.plot(t, phase2, color="blue", label="Phase 2")
plt.plot(t, phase3, color="green", label="Phase 2")
plt.title("Netzwerk a la Lennart")
plt.xlabel('$t$')
plt.ylabel('$Was-ist-mein-Y-Wert?$')
plt.show()
print("Danke Lennart :)")
