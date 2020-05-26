import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties.unumpy import uarray
from uncertainties import unumpy as unp

#Daten
N_U = np.array([129,143,144,136,139,126,158]) #Imp/300s
N_U_err = ufloat(np.mean(N_U),np.std(N_U, ddof=1))/10 #Imp/30s
t, N_V = np.genfromtxt('data/Vanadium.dat', delimiter=',', unpack=True)
N_V_d = N_V - unp.nominal_values(N_U_err)
N_V_dif = uarray(N_V_d, np.sqrt(N_V_d))

#Ausgleichsrechnung 1
def f(t,lam,b):
    return -lam * t + b
params, cov = curve_fit(f, t, np.log(unp.nominal_values(N_V_dif)), sigma=unp.std_devs(N_V_dif))
uncertainties = np.sqrt(np.diag(cov))
lam = ufloat(params[0],uncertainties[0])
b = ufloat(params[1],uncertainties[1])

#Ausgleichsrechnung 2
params2, cov2 = curve_fit(f, t[0:17], np.log(unp.nominal_values(N_V_dif[0:17])), sigma=unp.std_devs(N_V_dif[0:17]))
uncertainties2 = np.sqrt(np.diag(cov2))
lam2 = ufloat(params2[0],uncertainties2[0])
b2 = ufloat(params2[1],uncertainties2[1])

#Ausgabe
print('N_U_err =',N_U_err)
print('lam =',lam,'und b =',b)
print('T =',np.log(2)/lam)
print('lam2 =',lam2,'und b2 =',b2)
print('T =',np.log(2)/lam2)

#Plots
plt.xlabel(r'$t \,/\, s$')
plt.ylabel(r'$N \,/\, \frac{Imp}{s}$')
plt.plot(t,np.log(unp.nominal_values(N_V_dif)), 'b.', label='Messwerte')
plt.errorbar(t,np.log(unp.nominal_values(N_V_dif)),yerr=np.log(unp.std_devs(N_V_dif)), fmt='c,',label='Messfehler')
plt.plot(t,f(t,unp.nominal_values(lam),unp.nominal_values(b)), 'r-', label='Lineare Regression')
plt.grid()
plt.legend()
plt.show()