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
x, I_dun, I = (np.genfromtxt('data/doppelspalt.csv', delimiter=', ', unpack=True))

#Umrechnen in SI
x = x*10**-3 - 26*10**-3 + 10**-20 #um division durch null zu verhindern
l = 0.85
phi = x/l
I_0 = (I-I_dun)*10**-9
b = 0.1 # Breite Spalt in mm
g = 0.4 # Abstand spalt
print(I_0)
#Funktion
def fit(x, a, b, c):
    return a * (b/np.sin(x)) * np.sin(np.sin(x)/b) * np.cos(c * np.sin(x)) 

#Ausgelichsrechung
phi_plot = np.linspace(phi[0], phi[50], 5000)
prms, pcov = curve_fit(fit, phi, I_0, p0 = (8, 0.001, 1))

print('Parameter:')
for i,j,k in zip('abc', prms, np.diag(pcov)):
    print(f'{i} =  {j:.5f} +-  {np.sqrt(k):.5f}')

print('b= ', 633*10**-9/0.00241*np.pi)
print('g= ', 633*10**-9 *160.23067 /np.pi - 633*10**-9/0.00241*np.pi)

c_th = np.pi * (g + b) / (633*10**-9 * 1000)
b_th = 633*10**-9 * 1000 / np.pi / b 
a = 4
I_th = fit(phi_plot, a, b_th, c_th)

#Plotten
plt.plot(phi, I_0*10**9,  'r.', label = 'Messwerte-Doppelspalt')
plt.plot(phi_plot, fit(phi_plot, prms[0], prms[1], prms[2])*10**9, 'b-', label='Ausgleichsrechung')
plt.plot(phi_plot, I_th/np.max(I_th)*10**3.85, 'g-', label='Theorie')
plt.xlabel(r'$\varphi \;/\; rad$')
plt.ylabel(r'$I \; /\; nA$')
plt.grid()
plt.legend()
plt.savefig('data/doppelspalt.pdf')
plt.show()
