import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def func(T,a,b):
    return a * T + b

def theorie(f):
    w = 2 * np.pi * f
    w = w * 10**3 #hertz
    U0 = 175  *10**-3#volt
    L = 16.87 * 10**-3 #herny
    C = 2.060 * 10**-9 #kapazität
    R = 682
    return 1/( np.sqrt((1 - L * C * w**2)**2 + w**2 * R**2 * C**2))

t, U =np.genfromtxt('data/c2.csv', delimiter=',', unpack=True)
x = np.linspace(np.min(t), np.max(t), 1000)
U = U/175
plt.xlabel(r'$f \, / \, kHz$')
plt.ylabel(r'$ U_c \, / \, U_0 $')
plt.grid()
plt.plot(t, U,'rx', label='Messwerte')
plt.plot(x, theorie(x), 'b-', label='Theoriekurve')
plt.legend()
plt.savefig('plotc2.pdf')
plt.show()