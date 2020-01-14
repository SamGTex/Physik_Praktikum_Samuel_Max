import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import math as mp
f,a,b=np.genfromtxt('data/d.csv', delimiter=',', unpack=True)
phi = a/b * 2*np.pi

def phi_(f):
    w = 2 * np.pi * f
    w = w  *10**3#hertz
    U0 = 175  *10**(-3)#volt
    L = 16.87 * 10**(-3) #herny
    C = 2.060 * 10**(-9) #kapazität
    R = 682
    return np.arctan((-w * R * C)/(1 - L*C*w**2))
x = np.linspace(np.min(f), np.max(f), 1000)

print(phi)
plt.xlabel(r'$f \,/\, kHz$')
plt.ylabel(r'$ \varphi $')
plt.grid()
plt.plot(f, phi,'rx', label='Messwerte')
plt.plot(x, phi_(x), 'b-' , label='Theoriekurve')
plt.legend()
plt.savefig('plotd2.pdf')
plt.show()