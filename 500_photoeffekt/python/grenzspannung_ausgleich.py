import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties.unumpy import uarray
from uncertainties import unumpy as unp

#Funktion
def f(x,a,b):
    return a*x + b

c = 299792458 #m/s
h = 6.626 *10**(-34) #Js
e0 = -1.602 *10**(-19) #C
#577, -14
#546, -12
#434, -9.5
lam = np.array([577,546,434]) #nm
U = uarray([-14, -12, -9.5],[4,4,2.4]) #V
lam = lam*10**(-9) #m
v = c/lam #1/s

#Ausgleichsrechnung
popt, pcov = curve_fit(f,v, unp.nominal_values(U), sigma=unp.std_devs(U))
a=ufloat(popt[0],np.absolute(pcov[0][0])**0.5)
b=ufloat(popt[1],np.absolute(pcov[1][1])**0.5)
v_lin = np.linspace(np.min(v), np.max(v), 100) 

#Ausgabe
#a = h/e_0
#b = - A_k/e_0
print(v*10**(-12))
a_th = h/e0
abw = (a-a_th)*100/a_th 
print('Experimentel: h/e_0 =',a,', b =', b)
print('Theorie: h/e_0 =',a_th)
print('Abweichung:',abw,'%')

#Plots
plt.xlabel(r'$v \,/\, Hz$')
plt.ylabel(r'$U \,/\, V$')
plt.plot(v, unp.nominal_values(U), 'rx', label='Messwerte')
plt.plot(v_lin, f(v_lin,a.n,b.n), 'b-', label='Lineare Ausgleichsrechnung')
plt.legend()
plt.grid()
plt.savefig('build/grenzspannung_ausgleich.pdf')
plt.show()