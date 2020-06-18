import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

#Funktion
def f(x,a,b):
    return a*x + b

U, I = np.genfromtxt('data/violett.csv', comments='#', unpack=True, delimiter=',') #U in V, I in nA
I = I*10**(-9) #A

#Ausgleichsrechnung
popt, pcov = curve_fit(f,U,np.sqrt(I))
a=ufloat(popt[0],np.absolute(pcov[0][0])**0.5)
b=ufloat(popt[1],np.absolute(pcov[1][1])**0.5)
U_lin = np.linspace(np.min(U), np.max(U), 100) 

#Plots
plt.xlabel(r'$U \,/\, V$')
plt.ylabel(r'$I \,/\, A$')
plt.plot(U, np.sqrt(I), 'rx', label='Messwerte')
plt.plot(U_lin, f(U_lin,a.n,b.n), 'b-', label='Lineare Ausgleichsrechnung')
plt.legend()
plt.grid()
plt.savefig('build/violett.pdf')
plt.show()