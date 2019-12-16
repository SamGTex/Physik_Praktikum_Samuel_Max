import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def func(t,A_0,mu):
    return A_0*np.exp(-2*np.pi*mu*t)

t, U =np.genfromtxt('python/data/a.csv', delimiter=',', unpack=True)
U = U / 80
U_1 = abs(U)

plt.xlabel(r'$t \, / \, ms$')
plt.ylabel(r'$\ln \left ( U_c \,/\, U_0 \right ) $')
plt.grid()
plt.semilogx(t, U,'rx', label='Messwerte')

popt, pcov = curve_fit(func, t, U_1)
print(popt)
x=np.linspace(np.min(t), np.max(t), 100)
plt.plot(x, func(x,popt[0], popt[1]),'b-', label='Ausgleichsgrechnung')
plt.plot(x, func(x,-popt[0], popt[1]),'b-')
plt.legend(loc='center left')
plt.savefig('plota.pdf')
plt.show()