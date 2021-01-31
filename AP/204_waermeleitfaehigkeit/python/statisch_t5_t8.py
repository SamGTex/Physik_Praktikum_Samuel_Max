import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
N, T1, T2, T3, T4, T5, T6, T7, T8, s = (np.genfromtxt('data/statisch.txt', delimiter=', ', unpack=True))
T5 = T5[:117]
T8 = T8[:117]
s = s[:117]
plt.xlabel(r'$t \, / \, s$')
plt.ylabel(r'$T \, / \, °C$')
plt.grid()
plt.plot(s, T5, 'g-', label='T5')
plt.plot(s, T8, 'r-', label='T8')
plt.legend(loc='best')
plt.savefig('statsisch_T5_T8.pdf')
plt.show