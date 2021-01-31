import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties.unumpy import uarray
from uncertainties import unumpy as unp
from scipy.stats import sem

#Daten
N_U = np.array([129,143,144,136,139,126,158]) #Imp/300s
N_U_err = ufloat(np.mean(N_U),sem(N_U))/10 #Imp/30s
t, N_V = np.genfromtxt('data/Vanadium.dat', delimiter=',', unpack=True)
N_V_err = uarray(N_V, np.sqrt(N_V))
N_V_dif = N_V_err - N_U_err
N_V_log = unp.log(N_V_dif)

#Ausgleichsrechnung 1
def f(t,lam,b):
    return -lam * t + b
params, cov = curve_fit(f, t, unp.nominal_values(N_V_log), sigma=unp.std_devs(N_V_log))
uncertainties = np.sqrt(np.diag(cov))
lam = ufloat(params[0],uncertainties[0])
b = ufloat(params[1],uncertainties[1])

#Ausgleichsrechnung 2
params2, cov2 = curve_fit(f, t[0:17], unp.nominal_values(N_V_log[0:17]), sigma=unp.std_devs(N_V_log[0:17]))
uncertainties2 = np.sqrt(np.diag(cov2))
lam2 = ufloat(params2[0],uncertainties2[0])
b2 = ufloat(params2[1],uncertainties2[1])

#Ausgabe
T_th = 3.743*60 #s
T1 = np.log(2)/lam
T2 = np.log(2)/lam2

print(N_V_dif)
print('N_U_err =',N_U_err*10)
print('lam =',lam,'und b =',b)
print('T =',T1,', Abw. =',(T_th-T1)*100/T_th)
print('lam2 =',lam2,'und b2 =',b2)
print('T =',T2,', Abw. =',(T_th-T2)*100/T_th)

#Plots
plt.xlabel(r'$t \,/\, s$')
plt.ylabel(r'$N \,/\, \frac{Imp}{30 s}$')
plt.yscale('log')
plt.plot(t, unp.nominal_values(N_V_dif), 'b.', label='Messwerte')
plt.errorbar(t,unp.nominal_values(N_V_dif),yerr=unp.std_devs(N_V_dif), fmt='c,',label='Messfehler')
plt.plot(t,np.exp(f(t,unp.nominal_values(lam),unp.nominal_values(b))), 'r-', label='Lineare Regression')
plt.grid()
plt.legend()
plt.savefig('build/vanadium.pdf')
plt.show()