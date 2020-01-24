import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
N, T1, T2, T3, T4, T5, T6, T7, T8, s = (np.genfromtxt('data/dynamisch2.txt', delimiter=', ', unpack=True))
T7 = T7
T8 = T8
s = s
plt.xlabel(r'$t \, / \, s$')
plt.ylabel(r'$T \, / \, °C$')
plt.grid()
plt.plot(s, T7, 'g-', label='T7')
plt.plot(s, T8, 'r-', label='T8')
plt.legend(loc='best')
plt.savefig('dynamisch2_T7_T8.pdf')
plt.show()