import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

#Werte
Z_zn = 30
Z_ga = 31
Z_br = 35
Z_rb = 37
Z_sr = 38
Z_zr = 40
Z = np.array([30,31,35,37,38,40])

E_zn = 1.5382 * 10**(-15) #J
E_ga = 1.6584 * 10**(-15) #J
E_br = 2.1596 * 10**(-15) #J
E_rb = 2.4116 * 10**(-15) #J
E_sr = 2.5615 * 10**(-15) #J
E_zr = 2.8400 * 10**(-15) #J
E = np.array([1.5382,1.6584,2.1596,2.4116,2.5615,2.8400])*10**(-15)

#Konstanten
d = 201.4*10**(-12) #m
h = 6.626*10**(-34) #Js
c = 299792458 #m/s
R_inf_th = 13.6 * 1.602176634*10**(-19) #J

def f(x,a,b):
    return a*x+b

popt, cov = curve_fit(f,Z,np.sqrt(E))
uncertainties = np.sqrt(np.diag(cov))
a = ufloat(popt[0],uncertainties[0])
b = ufloat(popt[1],uncertainties[1])
R_ber = a**2/h
R_inf_ber = R_ber*h
print('R_ber =', R_ber)
print('R_inf_ber =', R_inf_ber)
print('R_inf_th =', R_inf_th)
print('Abweichung in %:', (R_inf_th-R_inf_ber)*100/R_inf_th)

lin = np.linspace(np.min(Z),np.max(Z),100)
plt.xlabel(r'$\mathrm{N}$')
plt.ylabel(r'$\sqrt{E_K \,/\, \mathrm{J}}$')
plt.plot(Z,np.sqrt(E),'bx',label='Messwerte')
plt.plot(lin,f(lin,a.n,b.n),'r-',label='Lineare Ausgleichsrechnung')
plt.legend()
plt.grid()
plt.savefig('build/ausgleich.pdf')
plt.show()