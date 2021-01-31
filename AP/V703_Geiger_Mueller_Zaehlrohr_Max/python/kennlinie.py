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

#Funktion fuer ausgleichsgerade
def func(x,a,b):
    return a*x+b


#einlesen der Werte
U, N = (np.genfromtxt('data/Kennlinie.dat', delimiter=', ', unpack=True))

#Fehler der Impulse berechnen
N_err = unp.uarray([N,np.sqrt(N)])

#Bestimmung der Plateau gerade es wird dabei nur von array eintrag 5-43 geplottet
#weil erst bei eintrag 5 das Plateau beginnt und bei 43 aufhoert
popt, pcov = curve_fit(func, U[5:33], unp.nominal_values(N_err[5:33]), sigma=unp.std_devs(N_err[5:33]),p0=[350,1000])
fehler = np.sqrt(np.diag(pcov))
a = ufloat(popt[0], fehler[0])
b = ufloat(popt[1], fehler[1])
print('Steigung a des Plateau: ',a,'Startwert b: ',b)

#Prozentuale Steigung berechnen

a_pro = (N_err[33]/N_err[5]  -1)*100 / (640-370) *100
print('prozentuale Steigung: ', a_pro)



#plotten
plt.xlabel(r'$U\, / \, V$')
plt.ylabel(r'$N\,/\,\frac{Imp}{60s}$')
plt.grid()
plt.errorbar(U, N, yerr=unp.std_devs(N_err) , fmt='r_', label='Impulse')
plt.plot(U[5:33], func(U[5:33], popt[0], popt[1]), 'k-', label='Ausgleichsgerade')
plt.legend(loc='best')
plt.savefig('kennlinie.pdf')
#plt.show()

#Bestimmung der Totzeit mit zwei Quellen Methode Aufgabe 2
N_tot = np.array([96041, 158479, 76518])
N_tot_err = unp.uarray([N_tot, np.sqrt(N_tot)])/120
T=(N_tot_err[0]+N_tot_err[2]-N_tot_err[1])/(2*N_tot_err[0]*N_tot_err[2])

print('Totzeit T:' , T)

