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

t, U =np.genfromtxt('data/c.csv', delimiter=',', unpack=True)
U = U/175
U_2 =np.linspace(640/(175*np.sqrt(2)), 640/(175*np.sqrt(2)), 100)
x=np.linspace(np.min(t), np.max(t), 100)
print(theorie(t))
plt.xlabel(r'$f \, / \, kHz$')
plt.ylabel(r'$ ln(U_c \, / \, U_0) $')
plt.grid()
plt.semilogx(t, U,'rx', label='Messwerte')
plt.semilogx(x, theorie(x), 'b-', label='Theoriekurve')
plt.legend()
plt.savefig('plotc.pdf')
plt.show()