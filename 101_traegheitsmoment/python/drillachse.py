import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
#Werte
phi, F = np.genfromtxt('data/stange.csv', comments='#', unpack=True, delimiter=',')
r, T = np.genfromtxt('data/gewichte.csv', comments='#', unpack=True, delimiter=',')
phi = np.radians(phi)
r_d=0.142 #m
r=r/100   #m
m=0.22327 #kg

#Funktionen
def T2(x):
    return a*x + b

#Rechnung für D
D = F*r/phi
D_mittel = ufloat(np.mean(D), np.std(D,ddof=1))
print('D: ', D)
print('D_mittel =', D_mittel)

#Rechnung für I_s
