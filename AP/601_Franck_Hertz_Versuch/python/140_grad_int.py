import numpy as np
import matplotlib.pyplot as plt

#Werte
U_a, I_A = np.genfromtxt('data/140_grad.csv', comments='#', unpack=True, delimiter=',')
I_A = I_A * 10**(-3) #nA

#Plots
plt.xlabel(r'$U_A \,/\, V$')
plt.ylabel(r'$I_A \,/\, nA$')
plt.plot(U_a,I_A,'rx',label='Messwerte')
plt.grid()
plt.legend()
plt.savefig('build/140_int.pdf')
plt.show()