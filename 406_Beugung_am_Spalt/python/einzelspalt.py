import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
#from scipy.interpolate import interp1d
#from scipy.signal import find_peaks
from scipy.stats import sem
import scipy.constants as cn
#from uncertainties import ufloat
#from uncertainties import unumpy as unp


#einlesen der Werte x-Ort des Messgerät, I_dun dunkelStrom, I strom mit laser
x, I_dun, I = (np.genfromtxt('data/einzelspalt.csv', delimiter=', ', unpack=True))

#Umrechnen in SI
x = x*10**-3 - 25.75*10**-3 + 10**-10 #um division durch null zu verhindern
l = 0.85
phi = x/l
I_0 = (I-I_dun)*10**-9
b = 0.1*10**-3
a=4



#Funktion
def B(x, a, b):
    return a * (b/np.sin(x))**2 * np.sin(np.sin(x)/b)**2

#Ausgleichsrechung
prms, pcov = curve_fit(B ,phi,I_0, p0 = (8, 0.1))
print(prms[0], prms[1])
print('b= ', 633*10**-9/ (np.pi*prms[1] ))
print(pcov)

#Theoriekurve

phi_plot = np.linspace(phi[0], phi[50], 5000)
b_th = 633*10**-9/ np.pi / b 
print(b_th)
B_theory = 4*np.sin(1/b_th*np.sin(phi_plot))**2 / (b_th*np.sin(phi_plot))**2
#print(B_theory[5])
#Plotten

plt.plot(phi, I_0*10**9,  'r.', label = 'Messwerte-Einzelspalt')
plt.plot(phi_plot, B(phi_plot, prms[0], prms[1])*10**9, 'b-', label='Ausgleichsrechung')
plt.plot(phi_plot, B_theory/np.max(B_theory)*10**3.9, color = 'green', label = 'Theorie-Einzelspalt')
plt.xlabel(r'$\varphi \;/\; rad$')
plt.ylabel(r'$I \; /\; nA$')
plt.grid()
plt.legend()
plt.savefig('data/einzelspalt.pdf')
plt.show()
