import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema
from scipy.stats import sem
from uncertainties import ufloat

#Werte
U_a, I_A = np.genfromtxt('data/franck_hertz_kurve.csv', comments='#', unpack=True, delimiter=',')
c =299792458 #m/s
h =6.626 * 10**(-34) #Js

#find maxima
max_indi = argrelextrema(I_A, np.greater)
max_indi = max_indi[0]
#max_indi = np.delete(max_indi,1,1)
print(max_indi)
print(U_a[max_indi])
print(I_A[max_indi])

#abstand maxima
dif = np.diff(U_a[max_indi])
dif_mittel = ufloat(np.mean(dif),sem(dif))
print('abstaende:',dif)
print('E = mittel =',dif_mittel, 'eV')
# h*v = E_1 - E_0 und lam = c/v
# => lam = c*h / (E_1-E_0)
lam = c*h/(dif_mittel*1.60218*10**(-19)) 
print('lambda =', lam*10**(9),'nm')

#Kontaktpotential
print('1. Max.: U_1 =', U_a[max_indi[0]])
print('K_2 =', U_a[max_indi[0]]-dif_mittel)

#plots
plt.xlabel(r'$U_a \,/\, V$')
plt.ylabel(r'$I_A \,/\, nA$')
plt.plot(U_a,I_A,'rx',label='Messwerte')
plt.scatter(U_a[max_indi],I_A[max_indi], s=80, facecolor='none',edgecolor='b' ,label='Maxima')
plt.grid()
plt.legend()
plt.savefig('build/franck_hertz.pdf')
plt.show()