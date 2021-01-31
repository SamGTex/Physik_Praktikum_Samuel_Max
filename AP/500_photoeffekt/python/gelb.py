import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

#Funktion
def f(x,a,b):
    return a*x + b

U, I = np.genfromtxt('data/gelb.csv', comments='#', unpack=True, delimiter=',') #U in V, I in nA
I = I*10**(-9) #A

#Ausgleichsrechnung
popt, pcov = curve_fit(f,U,np.sqrt(I))
a=ufloat(popt[0],np.absolute(pcov[0][0])**0.5)
b=ufloat(popt[1],np.absolute(pcov[1][1])**0.5)
U_lin = np.linspace(np.min(U), np.max(U), 100) 

#Ausgabe
print('a =',a)
print('b =',b)
print('U_g =', -b/a)

#Plots
plt.xlabel(r'$U \,/\, V$')
plt.ylabel(r'$\sqrt{I} \,/\, m\sqrt{A}$')
plt.plot(U, np.sqrt(I)*10**3, 'rx', label='Messwerte')
plt.plot(U_lin, f(U_lin,a.n,b.n)*10**3, 'b-', label='Lineare Ausgleichsrechnung')
plt.legend()
plt.grid()
plt.savefig('build/gelb.pdf')
plt.show()