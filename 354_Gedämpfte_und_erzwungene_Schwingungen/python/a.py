import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def func(A_0,mu,t):
    return A_0*math.exp**(-2*np.pi*mu*t)

t, U =np.genfromtxt('python/data/a.csv', delimiter=',', unpack=True)

plt.xlabel(r'$t \, / \, ms$')
plt.ylabel(r'$\ln \left ( U_c \right ) $')
plt.grid()
plt.semilogx(t, U,'rx', label='Messwerte')
plt.plot(t,func(A_0,mu,t),'b-',label='lineare Ausgleichsrechnung')
plt.legend()
plt.savefig('plota.pdf')
plt.show()


popt, pcov = curve_fit(func, t, U)
a1=popt[0]

print('RC =',-1/a1,'+-',RC_err)
print('b =',b1,'+-',b_err)
