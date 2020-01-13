import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

f, a , b  =np.genfromtxt('data/d.csv', delimiter=',', unpack=True)
phi = a/b * 2*np.pi
def phi_(f):
    w = 2 * np.pi * f
    w = w  *10**3#hertz
    U0 = 175  *10**-3#volt
    L = 16.87 * 10**-3 #herny
    C = 2.060 * 10**-9 #kapazität
    R = 682
    return np.arctan(w * R * C/(1-L*C*w**2))

x = np.linspace(np.min(f), np.max(f), 1000)

plt.xlabel(r'$f \,/\, kHz$')
plt.ylabel(r'$ ln(\varphi) $')
plt.grid()
plt.semilogx(f, phi,'rx', label='Messwerte')
plt.semilogx(x, phi_(x), 'b-', label='Theoriekurve')
plt.semilogx(x2, phi_(x2)+1.5, 'b-', label='Theoriekurve')
plt.legend()
plt.savefig('plotd.pdf')
plt.show()