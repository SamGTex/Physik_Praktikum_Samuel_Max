import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties.unumpy import uarray
from uncertainties import unumpy as unp

#Daten
N_U = np.array([129,143,144,136,139,126,158]) #Imp/300s
N_U_err = ufloat(np.mean(N_U),np.std(N_U, ddof=1))/10 #Imp/30s
t, N_R = np.genfromtxt('data/Rhodium.dat', delimiter=',', unpack=True)
N_R_d = N_R - unp.nominal_values(N_U_err)
N_R_dif = uarray(N_R_d, np.sqrt(N_R_d))
print(N_R_dif)
def f(t,lam,b):
    return -lam * t + b
#Ausgleichsrechnung mit werten des langsamen zerfalls
#42 wird dabei raus genommen weil der wert negativ ist
params, cov = curve_fit(f, t[20:], np.log(unp.nominal_values(N_R_dif[20:])), sigma=unp.std_devs(N_R_dif[20:]))
uncertainties = np.sqrt(np.diag(cov))
lam = ufloat(params[0],uncertainties[0])
b = ufloat(params[1],uncertainties[1])

#Array mit werten des langsamen zerfalls
N_R_slow =f(t, unp.nominal_values(lam),unp.nominal_values(b) )
#Ausgleichsrechnung mit schnellem zerfall, dabei wird langsamer zerfall abgezogen
params2, cov2 = curve_fit(f, t[:20], np.log(unp.nominal_values(N_R_dif[:20])- N_R_slow[:20]), sigma=unp.std_devs(N_R_dif[:20]-N_R_slow[:20]))
uncertainties2 = np.sqrt(np.diag(cov2))
lam2 = ufloat(params2[0],uncertainties2[0])
b2 = ufloat(params2[1],uncertainties2[1])

#Ausgabe
print('Slow: lam =',lam,', b =', b, ', T =',np.log(2)/lam)
print('Fast: lam =',lam2,', b =', b2, ', T =',np.log(2)/lam2)


#Plots
plt.xlabel(r'$t \,/\, s$')
plt.ylabel(r'$N \,/\, \frac{Imp}{s}$')
plt.plot(t,np.log(unp.nominal_values(N_R_dif)), 'b.', label='Messwerte')
plt.plot(t, f(t, unp.nominal_values(lam),unp.nominal_values(b) ), label='Ausgleichsgerade, langsamer Zerfall')
plt.plot(t[0:20], f(t[0:20], unp.nominal_values(lam2),unp.nominal_values(b2) ), label='Ausgleichsgerade, schneller Zerfall')
plt.grid()
plt.legend(loc='best')
plt.show()