import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

#Funktionen
def T2(r2,a,b):
    return a*r2 + b

#Werte
phi, F = np.genfromtxt('data/stange.csv', comments='#', unpack=True, delimiter=',')
r, T = np.genfromtxt('data/gewichte.csv', comments='#', unpack=True, delimiter=',')
phi = np.radians(phi)
r_d=0.142 #m
r=r/100   #m
m=0.22327 #kg
R_z=1.75/100 #m
h_z=3/100 #m

#Rechnung für D
D = F*r/phi
D_mittel = ufloat(np.mean(D), np.std(D,ddof=1))
print('D: ', D)
print('D_mittel =', D_mittel)

#Rechnung für I_s
popt, pcov = curve_fit(T2,r**2,T**2)
a=ufloat(popt[0],np.absolute(pcov[0][0])**0.5)
b=ufloat(popt[1],np.absolute(pcov[1][1])**0.5)
I_d=D_mittel*b/(2*np.pi)**2- 2*m*(R_z**2/4 + h_z**2/12)
a_all=8*np.pi**2*m/D
print('a:',a)
print('b:',b)
print('I_d:',I_d)
plt.xlabel(r'$a^2/m^2$')
plt.ylabel(r'$T^2/Hz^2$')
x=np.linspace(np.min(r**2),np.max(r**2),100)
plt.plot(x,a.n*x+b.n,'b-',label='lineare Ausgleichsrechnung')
plt.plot(r**2,T**2,'rx',label='Messwerte')
plt.grid()
plt.legend()
plt.show()