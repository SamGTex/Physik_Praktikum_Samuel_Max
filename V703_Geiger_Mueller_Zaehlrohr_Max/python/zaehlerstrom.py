import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d
from scipy.signal import find_peaks
from scipy.stats import sem
import scipy.constants as cn
from uncertainties import ufloat
from uncertainties import unumpy as unp

U_I, I = (np.genfromtxt('data/Zaehlrohrstrom.dat', delimiter=', ', unpack=True))

def func(x,a,b):
    return x*a+b
#N werte aus tabelle abgelesen
N = np.array([9837, 9995, 10264, 10151, 10184, 10253, 10493, 11547])
#I hat der Fehler 0.05
I_err = unp.uarray(I, 0.05)
#print('I_err: ', I_err)

#N hat den fehler sqrt(N)
N_err = unp.uarray(N, np.sqrt(N))/60
#print('N_err: ',N_err)

#Berechnung des mittleren zaehlerstroms mit fehlern
Z = I_err/(cn.e*N_err)
#print('Z: ', Z)

popt, pcov = curve_fit(func, I, unp.nominal_values(Z), sigma=unp.std_devs(Z),p0=(10**15, 10**15))
fehler = np.sqrt(np.diag(pcov))
a = ufloat(popt[0], fehler[0])
b = ufloat(popt[1], fehler[1])

print('Z ist gleich a also :',a,'und b ist gleich: ', b)  

x = np.linspace(I[0], I[7])

#plotten
plt.xlabel(r'$I\, / \, \mu A$')
plt.ylabel(r'$Z\cdot10^{16}$')
plt.grid()
plt.errorbar(I, unp.nominal_values(Z)/10**16, yerr=unp.std_devs(Z)/10**16 , fmt='r_', label='freigesetzte Ladungen')
plt.plot(x, func(x, popt[0], popt[1])/10**16, 'k-', label='Ausgleichsgerade')
plt.legend(loc='best')
plt.savefig('zaehlstrom.pdf')
plt.show()