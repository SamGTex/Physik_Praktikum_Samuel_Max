import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def func(T,a,b):
    return a * T + b

t, U =np.genfromtxt('python/data/c.csv', delimiter=',', unpack=True)
U = U/175
U_2 =np.linspace(640/(175*np.sqrt(2)), 640/(175*np.sqrt(2)), 100)
x=np.linspace(np.min(t), np.max(t), 100)
plt.plot(x, U_2, 'g-')
plt.xlabel(r'$f \, / \, Hz$')
plt.ylabel(r'$ U_c \, / \, U_0 $')
plt.grid()
plt.semilogx(t, U,'rx', label='Messwerte')
plt.legend()
plt.savefig('plotc.pdf')
plt.show()