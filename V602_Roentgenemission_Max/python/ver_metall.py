import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
#from scipy.interpolate import interp1d
#from scipy.signal import find_peaks
#from scipy.stats import sem
import scipy.constants as cn
from uncertainties import ufloat
#from uncertainties import uarray
from uncertainties import unumpy as unp


theta_z , N_z = np.genfromtxt('data/Zink.dat', delimiter=',', unpack=True)
theta_g , N_g = np.genfromtxt('data/Gallium.dat', delimiter=',', unpack=True)
theta_b , N_b = np.genfromtxt('data/Brom.dat', delimiter=',', unpack=True)
theta_r , N_r = np.genfromtxt('data/Rubidium.dat', delimiter=',', unpack=True)
theta_s , N_s = np.genfromtxt('data/Strontium.dat', delimiter=',', unpack=True)
theta_zi , N_zi = np.genfromtxt('data/Zirkonium.dat', delimiter=',', unpack=True)

#Ordnungszahlen
Z_zink = 30
Z_gall = 31
Z_brom = 35
Z_rubi = 37
Z_stron = 38
Z_zirk = 40

#Funktionen

#Geraden funktion für curve fir
def func(x, a, b):
    return a*x + b

#Rydbergfrequenz berechnen
def ryd(sigma, z, Ek):
    return Ek / (cn.h *(z-sigma)**2)

#Ik kante berechnen
def Ik_kante(In_min, In_max):
    return In_min + (In_max - In_min)/2

#winkel mit bragg bedingnung in wellenlaenge
def wave(theta):
    d = 201.4 * 10**(-12)
    n = 1
    return 2*d*np.sin(np.radians(theta)) / n 

#abschirmkonstante sigma durch ordnungszahl und energie
def abschirm(Z, E_K):
    R = 13.6 * cn.e
    return Z - np.sqrt(E_K/R - (cn.alpha**2 * Z**4 )/ 4)

#Intentsität max bestimmen
In_max_zink = np.amax(N_z)
In_max_gall = np.amax(N_g)
In_max_brom = np.amax(N_b)
In_max_rubi = np.amax(N_r)
In_max_stron = np.amax(N_s)
In_max_zirk = np.amax(N_zi)

#Intentsität min bestimmen
In_min_zink = np.amin(N_z)
In_min_gall = np.amin(N_g)
In_min_brom = np.amin(N_b)
In_min_rubi = np.amin(N_r)
In_min_stron = np.amin(N_s)
In_min_zirk = np.amin(N_zi)

#IK kanten berechnung(y werte):
Ik_kan_zink = Ik_kante(In_min_zink, In_max_zink)
Ik_kan_gall = Ik_kante(In_min_gall, In_max_gall)   
Ik_kan_brom = Ik_kante(In_min_brom, In_max_brom)   
Ik_kan_rubi = Ik_kante(In_min_rubi, In_max_rubi)   
Ik_kan_stron = Ik_kante(In_min_stron, In_max_stron)   
Ik_kan_zirk = Ik_kante(In_min_zirk, In_max_zirk)

#Bestimmung der Theta Winkel des Wertes der am nächten an den richtigem IK Wert liegt
Ik_xy_zink = np.array([18.7, 84.0])
Ik_xy_gall = np.array([17.4, 102.0])
Ik_xy_brom = np.array([13.2, 18.0])
Ik_xy_rubi = np.array([11.8, 39.0])
Ik_xy_stron =np.array([11.1, 120.0])
Ik_xy_zirk = np.array([10.0, 225.0])

#Energie an den Ik Kanten
Ek_zink = cn.c * cn.h / wave(Ik_xy_zink[0])
Ek_gall = cn.c * cn.h / wave(Ik_xy_gall[0])
Ek_brom = cn.c * cn.h / wave(Ik_xy_brom[0])
Ek_rubi = cn.c * cn.h / wave(Ik_xy_rubi[0])
Ek_stron = cn.c * cn.h / wave(Ik_xy_stron[0])
Ek_zirk= cn.c * cn.h / wave(Ik_xy_zirk[0])

#Bestimmung der Abschirmkonstanten
sigma_zink = abschirm(Z_zink, Ek_zink)
sigma_gall = abschirm(Z_gall, Ek_gall)
sigma_brom = abschirm(Z_brom, Ek_brom)
sigma_rubi = abschirm(Z_rubi, Ek_rubi)
sigma_stron = abschirm(Z_stron, Ek_stron)
sigma_zirk = abschirm(Z_zirk, Ek_zirk)

#Rydbergfrequenzen
F_Ryd_zink = ryd(sigma_zink, Z_zink, Ek_zink)
F_Ryd_gall = ryd(sigma_gall , Z_gall, Ek_gall) 
F_Ryd_brom = ryd(sigma_brom , Z_brom, Ek_brom) 
F_Ryd_rubi = ryd(sigma_rubi , Z_rubi, Ek_rubi) 
F_Ryd_stron = ryd(sigma_stron , Z_stron, Ek_stron) 
F_Ryd_zirk = ryd(sigma_zirk , Z_zirk, Ek_zirk) 

#Rydbergenergie
E_Ryd_zink = F_Ryd_zink * cn.h
E_Ryd_gall = F_Ryd_gall * cn.h
E_Ryd_brom = F_Ryd_brom * cn.h
E_Ryd_rubi = F_Ryd_rubi * cn.h
E_Ryd_stron = F_Ryd_stron * cn.h
E_Ryd_zirk = F_Ryd_zirk * cn.h

#Energien ausgeben
print ('Energieen an den K Kanten: Zink :', Ek_zink, 'Gallium :', Ek_gall, 'Brom :', Ek_brom, 'Rubidium :', Ek_rubi, 'Strontium :', Ek_stron, 'Zirkonium', Ek_zirk, '\n')
#Abschirmkonstanten ausgeben
print ('Abschrimkonstanten an den K Kanten: Zink :', sigma_zink, 'Gallium :', sigma_gall, 'Brom :', sigma_brom, 'Rubidium :', sigma_rubi, 'Strontium :', sigma_stron, 'Zirkonium', sigma_zirk,'\n')
#Rydbergenrgieen ausgeben
print('Rydbergenergien Zink :', E_Ryd_zink, 'Gallium :', E_Ryd_gall, 'Brom :', E_Ryd_brom, 'Rubidium :', E_Ryd_rubi, 'Strontium :', E_Ryd_stron, 'Zirkonium', E_Ryd_zirk,'\n')

plt.xlabel(r'$\theta \,/\, \degree$')
plt.ylabel(r'$N \,/\, \frac{Imp}{s}$')
plt.grid()

#plot der werte

plt.plot(theta_z,N_z,'.',label='Zink')
plt.plot(theta_g,N_g,'.',label='Gallium')
plt.plot(theta_b,N_b,'.',label='Brom')
plt.plot(theta_r,N_r,'.',label='Rubidium')
plt.plot(theta_s,N_s,'.',label='Strontium')
plt.plot(theta_zi,N_zi,'.',label='Zirkonium')
#plot der ik kanten

plt.plot(Ik_xy_zink[0] , Ik_xy_zink[1],'rx',label=r'$I_k$' ' Kanten')
plt.plot(Ik_xy_gall[0] , Ik_xy_gall[1],'rx')
plt.plot(Ik_xy_brom[0] , Ik_xy_brom[1],'rx')
plt.plot(Ik_xy_rubi[0] , Ik_xy_rubi[1],'rx')
plt.plot(Ik_xy_stron[0] , Ik_xy_stron[1],'rx')
plt.plot(Ik_xy_zirk[0] , Ik_xy_zirk[1],'rx')
plt.legend(loc='best',)
plt.savefig('verschmetalle.pdf')
#plt.show()
plt.clf()

#array mit den ek energien und den ordnungszahlen
ek_array = np.array([Ek_zink, Ek_gall, Ek_brom, Ek_rubi, Ek_stron, Ek_zirk])
z_array = np.array([Z_zink, Z_gall, Z_brom, Z_rubi, Z_stron, Z_zirk])

#curvefit von den energien
popt, pcov = curve_fit(func, z_array ,np.sqrt(ek_array))
fehler = np.sqrt((np.absolute(pcov)))
a = ufloat(popt[0], fehler[0][0])
b = ufloat(popt[1], fehler[1][1])

#Rydbergenergie ausgeben
print('Rydbergenergie ', a**2 / cn.e)

#plot der ausgleichsgeraden
plt.xlabel('Ordnungszahl Z')
plt.ylabel(r'$\sqrt{E_k}\, / \, \sqrt{J}$')
plt.grid()
plt.plot(z_array, np.sqrt(ek_array), 'rx', label=r'$E_k\,\, der\,\, Stoffe$')
plt.plot(z_array, func(z_array, popt[0], popt[1]), 'g-', label='Ausgleichsgerade')
plt.legend()
plt.savefig('ausgleichsgerade.pdf')
#plt.show()