import numpy as np
import matplotlib.pyplot as plt

U_a, I_A = np.genfromtxt('data/raumtemperatur.csv', comments='#', unpack=True, delimiter=',') #V,nA
I_A=I_A*10**(-9) #A
U_dif = (U_a[1:]-U_a[:12])
I_dif = (I_A[1:]-I_A[:12])
steigung = np.abs(I_dif/U_dif)
print(U_dif)
print(I_dif)
plt.xlabel(r'$U_a \,/\, V$')
plt.ylabel(r'$|\frac{\Delta U_a}{\Delta I_a}| \,/\, \frac{V}{A}$')
plt.grid()
plt.plot(U_a[:12],steigung,'rx')
plt.show()