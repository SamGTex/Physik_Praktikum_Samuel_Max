import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat
from uncertainties.unumpy import uarray
from uncertainties import unumpy as unp

#werte
U, N = np.genfromtxt('data/Kennlinie.dat', delimiter=',', unpack=True)
t = 60 #s
N_err = uarray(N,np.sqrt(N))/t

#ausgleichsgerade
U_ger = U[5:33]
N_ger = N_err[5:33]

def N_fkt(U_ger,a,b):
    return a * U_ger + b

params, cov = curve_fit(N_fkt, U_ger, unp.nominal_values(N_ger), sigma=unp.std_devs(N_ger))
uncertainties = np.sqrt(np.diag(cov))
a = ufloat(params[0],uncertainties[0])
b = ufloat(params[1],uncertainties[1])

lin_U = np.linspace(np.min(U_ger),np.max(U_ger),100)
print('Ausgleichsgerade: a =',a,', b =',b)
print('Steigung:',(N_fkt(100,a,b)-b)*100/(b),'%/100V')

#plots
plt.xlabel(r'$U \,/\, V$')
plt.ylabel(r'$N \,/\, \frac{Imp}{60 s}$')
plt.plot(U,unp.nominal_values(N_err),'bo',label='Messwerte')
plt.errorbar(U,unp.nominal_values(N_err),yerr=unp.std_devs(N_err), fmt='c,',label='Messfehler')
plt.plot(lin_U, N_fkt(lin_U,a.n,b.n), 'r-', label='Ausgleichsgerade')
plt.legend()
plt.grid()
plt.savefig('build/charakteristik.pdf')
plt.show()