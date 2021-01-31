import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

#Konstanten
e_0 = 1.602176634*10**(-19) #C
k_B = 1.380649*10**(-23) #J/K

#Funktionen
def j(U,a,T):
    return a*np.exp(-e_0*U/(k_B*T))

#Werte
U, I = np.genfromtxt('data/bremsspannung.csv', comments='#', unpack=True, delimiter=',') #V,nA
R_innen = 10**6 #Ohm
I = I/10**9 #A
U_k = U - R_innen*I #V

#Ausgleichsrechnung
popt, pcov = curve_fit(j,U_k,I,p0=[1,1000])
a=ufloat(popt[0],np.absolute(pcov[0][0])**0.5)
T=ufloat(popt[1],np.absolute(pcov[1][1])**0.5)
U_lin = np.linspace(np.min(U_k),np.max(U_k),1000)

#Ausgabe
print('U_korrigiert:',U_k)
print('a =',a,'und T =',T,'K')

#Plots
plt.xlabel(r'$U \,/\, V$')
plt.ylabel(r'$I \,/\, nA$')
plt.plot(U_k,I*10**9,'rx',label='Messwerte')
plt.plot(U_lin,j(U_lin,a.n,T.n)*10**9,'k-',label='Ausgleichsrechnung')
plt.grid()
plt.legend()
plt.savefig('build/anlaufgebiet.pdf')
plt.show()