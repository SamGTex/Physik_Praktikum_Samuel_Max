import numpy as np
import matplotlib.pyplot as plt

#Werte
U_a, I_A = np.genfromtxt('data/raumtemperatur.csv', comments='#', unpack=True, delimiter=',')

#Plots
plt.xlabel(r'$U_A \,/\, V$')
plt.ylabel(r'$I_A \,/\, nA$')
plt.plot(U_a,I_A,'rx',label='Messwerte')
plt.grid()
plt.legend()
plt.savefig('build/raumtemperatur_int.pdf')
plt.show()