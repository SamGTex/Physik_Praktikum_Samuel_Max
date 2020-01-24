import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
N, T1, T2, T3, T4, T5, T6, T7, T8, s = (np.genfromtxt('data/statisch.txt', delimiter=', ', unpack=True))
T1 = T1[:118]
T4 = T4[:118]
s = s[:118]
plt.xlabel(r'$t \, / \, s$')
plt.ylabel(r'$T \, / \, °C$')
plt.grid()
plt.plot(s, T1, 'g-', label='T1')
plt.plot(s, T4, 'r-', label='T4')
plt.legend(loc='best')
plt.savefig('statsisch_T1_T4.pdf')
plt.show