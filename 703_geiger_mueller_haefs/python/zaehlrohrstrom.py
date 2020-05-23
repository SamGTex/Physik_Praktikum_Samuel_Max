import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties.unumpy import uarray
from uncertainties import unumpy as unp
from uncertainties import ufloat

#Werte
U, I = np.genfromtxt('data/Zaehlrohrstrom.dat', delimiter=',', unpack=True)
t = 60 #s
I_err = uarray(I,0.05) * 10**(-6)
I = I * 10**(-6) #A
N_n = np.array([9837,9995,10264,10151,10184,10253,10493,11547])
N = uarray(N_n,np.sqrt(N_n)) / t #Imp/s
e0 = 1.602176462*10**(-19) #C

#Rechnungen
Z = I_err/(e0*N)
print(Z)

#Ausgleichsgerade
def f(I,a,b):
    return I * a + b

params, cov = curve_fit(f, I, unp.nominal_values(Z), sigma=unp.std_devs(Z), p0=[10**(10),10**(10)])
uncertainties = np.sqrt(np.diag(cov))
a = ufloat(params[0],uncertainties[0])
b = ufloat(params[1],uncertainties[1])
print('a =',a,', b =',b)
lin_I = np.linspace(np.min(I),np.max(I),8)

#Plots
plt.xlabel(r'$I \,/\, \mu A$')
plt.ylabel(r'$Z \,/\, \frac{1}{Imp}$')
plt.plot(I*10**6,unp.nominal_values(Z),'bx',label='Messergebnisse')
plt.plot(lin_I*10**6,f(lin_I,a.n,b.n),'r-',label='Ausgleichsgerade')
plt.legend()
plt.grid()
plt.savefig('build/zaehlrohrstrom.pdf')
plt.show()