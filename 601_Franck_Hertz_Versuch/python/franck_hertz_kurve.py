import numpy as np
import matplotlib.pyplot as plt

U_a, I_A = np.genfromtxt('data/franck_hertz_kurve.csv', comments='#', unpack=True, delimiter=',')

plt.plot(U_a,I_A,'rx',label='Messwerte')
plt.show()