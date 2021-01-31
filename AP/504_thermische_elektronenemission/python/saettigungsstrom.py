import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

#Funktionen
def j(U,I_S,A,B):
    return I_S-A*np.exp(-B*U)

#Werte
U_20, I_20 = np.genfromtxt('data/2A.csv', comments='#', unpack=True, delimiter=',')
U_22, I_22 = np.genfromtxt('data/2_2A.csv', comments='#', unpack=True, delimiter=',')
U_24, I_24 = np.genfromtxt('data/2_4A.csv', comments='#', unpack=True, delimiter=',')

I_20 = I_20*1000
I_22 = I_22*1000
I_24 = I_24*1000

#Saettigungsstrom
#Ausgleichsrechnung für I_f=2A
popt_20, pcov_20 = curve_fit(j,U_20[2:],I_20[2:],p0=[2.3,2.5,0])
I_s_20=ufloat(popt_20[0],np.absolute(pcov_20[0][0])**0.5)
A_20=ufloat(popt_20[1],np.absolute(pcov_20[1][1])**0.5)
B_20=ufloat(popt_20[2],np.absolute(pcov_20[2][2])**0.5)
#Ausgleichsrechnung für I_f=2.2A
popt_22, pcov_22 = curve_fit(j,U_22[6:],I_22[6:],p0=[500,100,0])
I_s_22=ufloat(popt_22[0],np.absolute(pcov_22[0][0])**0.5)
A_22=ufloat(popt_22[1],np.absolute(pcov_22[1][1])**0.5)
B_22=ufloat(popt_22[2],np.absolute(pcov_22[2][2])**0.5)
#Ausgleichsrechnung für I_f=2.4A
popt_24, pcov_24 = curve_fit(j,U_24[17:],I_24[17:],p0=[900,200,0])
I_s_24=ufloat(popt_24[0],np.absolute(pcov_24[0][0])**0.5)
A_24=ufloat(popt_24[1],np.absolute(pcov_24[1][1])**0.5)
B_24=ufloat(popt_24[2],np.absolute(pcov_24[2][2])**0.5)

#Ausgabe
print('Sättigungsstrom:')
print('für 2A: I_S =',I_s_20)
print('für 2.2A: I_S =',I_s_22)
print('für 2.4A: I_S =',I_s_24)

#Plots
plt.xlabel(r'$U \,/\, V$')
plt.ylabel(r'$I \,/\, mA$')

plt.plot(U_20,I_20,'rx',label='2.0 A')
plt.plot(U_22,I_22,'bx',label='2.2 A')
plt.plot(U_24,I_24,'gx',label='2.4 A')

U_lin_20 = np.linspace(np.min(U_20[2:]),np.max(U_20[2:]),1000)
U_lin_22 = np.linspace(np.min(U_22[6:]),np.max(U_22[6:]),1000)
U_lin_24 = np.linspace(np.min(U_24[17:]),np.max(U_24[17:]),1000)
plt.plot(U_lin_20,j(U_lin_20,I_s_20.n,A_20.n,B_20.n),'k-',label='Ausgleichsrechnung')
plt.plot(U_lin_22,j(U_lin_22,I_s_22.n,A_22.n,B_22.n),'k-')
plt.plot(U_lin_24,j(U_lin_24,I_s_24.n,A_24.n,B_24.n),'k-')
plt.grid()
plt.legend()
plt.savefig('build/saettigungsstrom.pdf')
plt.show()