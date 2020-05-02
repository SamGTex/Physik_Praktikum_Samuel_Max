import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d
from scipy.signal import find_peaks
from scipy.stats import sem
import scipy.constants as cn
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

#lineare regression
def func(x,a,b):
    return a*x+b
popt, pcov = curve_fit(func, lamda_al, T)
print(popt)
a = popt[0]
b = popt[1]

plt.xlabel(r'$\lambda \, / \, pm$')
plt.ylabel(r'$T(\lambda)$')
plt.grid()
plt.plot(lamda_al, T, 'rx', label='Transmission')
plt.plot(lamda_al, func(lamda_al, a, b), 'g-', label='Ausgleichsgerade')
plt.legend(loc='best')
plt.savefig('Transmission.pdf')
plt.show()

I_0 = 2731
I_1 = 1180
I_2 = 1024

T_1 = I_1/I_0
T_2 = I_2/I_0

def wave(T, a, b):
    return (T-b)/a

print('Die Wellenlänge lambda 1 entspricht: ', wave(T_1, a, b))
print('Die Wellenlänge lambda 2 entspricht: ', wave(T_2, a, b))