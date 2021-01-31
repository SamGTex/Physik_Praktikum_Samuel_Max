import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d
from scipy.signal import find_peaks
from scipy.stats import sem
import scipy.constants as cn
from uncertainties import ufloat
#from uncertainties import uarray
from uncertainties import unumpy as unp
#einlesung der Daten 
alpha_al , N_al = (np.genfromtxt('data/ComptonAl.txt', delimiter=', ', unpack=True))
alpah_0 , N_0 = (np.genfromtxt('data/ComptonOhne.txt', delimiter=', ', unpack=True))

#definition einiger groessen die in der anleitung gegeben waren
d = 201.4 * 10**(-12)
n = 1
t = 90 * 10**(-6)

#berechnung der Intentsitäten
I_al = N_al /(1 - t * N_al)
I_0 = N_0 / (1- t * N_0)

#umrechnung von grad zu rad
def rad(theta):
    return theta*2*np.pi / 360

#berechnung der Wellenlänge
lamda_al = 2*d*np.sin(rad(alpha_al)) / n

#umrechnung in pm  
lamda_al = lamda_al * 10**12

#lamda_0 = 2*d*np.sin(alpha_0) / n

#berechnung der Transmission
T = I_al/ I_0



#Fehler berechnung
N_al = unp.uarray(N_al, np.sqrt(N_al*300)/300)
N_0 = unp.uarray(N_0, np.sqrt(N_0*300)/300)

I_al_err = N_al /(1 - t * N_al)
I_0_err = N_0 / (1- t * N_0)
T_err = I_al_err/I_0_err

#lineare regression
def func(x,a,b):
    return a*x+b
popt, pcov = curve_fit(func, lamda_al, unp.nominal_values(T_err), sigma=unp.std_devs(T_err),p0=[0.5,50])
fehler = np.sqrt(np.diag(pcov))
a = ufloat(popt[0], fehler[0])
b = ufloat(popt[1], fehler[1])


#plotten

plt.xlabel(r'$\lambda \, / \, pm$')
plt.ylabel(r'$T(\lambda)$')
plt.grid()
plt.errorbar(lamda_al, T, yerr=unp.std_devs(T_err) , fmt='r_', label='Transmission')
plt.plot(lamda_al, func(lamda_al, popt[0], popt[1]), 'g-', label='Ausgleichsgerade')
plt.legend(loc='best')
plt.savefig('Transmission.pdf')
plt.show()

I_0 = 2731
I_1 = 1180
I_2 = 1024

T_1 = I_1/I_0
T_2 = I_2/I_0
print(T_1, T_2)
def wave(T, a, b):
    return (T-b)/a
print('der wert für die Steigung ', a, ' der startwert b ', b)
print('Die Wellenlänge lambda 1 entspricht: ', wave(T_1, a, b))
print('Die Wellenlänge lambda 2 entspricht: ', wave(T_2, a, b))
print('Damit erhält man eine Comptonwellenlänge von ', wave(T_2,a,b)-wave(T_1, a, b))