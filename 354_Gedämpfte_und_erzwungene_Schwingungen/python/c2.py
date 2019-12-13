import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def func(T,a,b):
    return a * T + b

t, U =np.genfromtxt('python/data/c2.csv', delimiter=',', unpack=True)
U = U/175
plt.xlabel(r'$t \, / \, ms$')
plt.ylabel(r'$ U_c \, / \, U_0 $')
plt.grid()
plt.plot(t, U,'rx', label='Messwerte')
plt.legend()
plt.savefig('plotc2.pdf')
plt.show()