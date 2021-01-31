import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

#Funktionen
def j(U,a,b):
    return a*U**b

#Werte
U, I = np.genfromtxt('data/2_4A.csv', comments='#', unpack=True, delimiter=',')
I = I/1000 #A

#Raumladungsgebiet: 0-60 V
I=I[:13]
U=U[:13]

#Ausgleichsrechnung
popt, pcov = curve_fit(j,U,I)
a=ufloat(popt[0],np.absolute(pcov[0][0])**0.5)
b=ufloat(popt[1],np.absolute(pcov[1][1])**0.5)
U_lin = np.linspace(np.min(U),np.max(U),1000)

#Ausgabe
print('Exponent b =',b)
print('a =',a)

#Plots
plt.xlabel(r'$U \,/\, V$')
plt.ylabel(r'$I \,/\, mA$')
plt.plot(U,I*1000,'rx',label='Messwerte')
plt.plot(U_lin,j(U_lin,a.n,b.n)*1000,label='Ausgleichsrechnung')
plt.grid()
plt.legend()
plt.savefig('build/langmuir.pdf')
plt.show()