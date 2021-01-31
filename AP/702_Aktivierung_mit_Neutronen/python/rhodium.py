import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties.unumpy import uarray
from uncertainties import unumpy as unp
from scipy.stats import sem

#Daten
N_U = np.array([129,143,144,136,139,126,158]) #Imp/300s
N_U_err = ufloat(np.mean(N_U),sem(N_U))/20 #Imp/15s
t, N_R = np.genfromtxt('data/Rhodium.dat', delimiter=',', unpack=True)
N_R_err = uarray(N_R, np.sqrt(N_R))
N_R_dif = N_R_err - N_U_err
N_R_log = unp.log(N_R_dif)

def f(t,lam,b):
    return -lam * t + b

#Ausgleichsrechnung mit werten des langsamen zerfalls
#42 wird dabei raus genommen weil der wert negativ ist
params, cov = curve_fit(f, t[17:], unp.nominal_values(N_R_log[17:]), sigma=unp.std_devs(N_R_log[17:]))
uncertainties = np.sqrt(np.diag(cov))
lam = ufloat(params[0],uncertainties[0])
b = ufloat(params[1],uncertainties[1])

#Array mit werten des langsamen zerfalls
N_R_slow_f = unp.exp(f(t, lam, b))
N_R_fast = N_R_dif - N_R_slow_f
N_R_fast_log = unp.log(N_R_fast[:14])

#Ausgleichsrechnung mit schnellem zerfall, dabei wird langsamer zerfall abgezogen
params2, cov2 = curve_fit(f, t[:14], unp.nominal_values(N_R_fast_log), sigma=unp.std_devs(N_R_fast_log))
uncertainties2 = np.sqrt(np.diag(cov2))
lam2 = ufloat(params2[0],uncertainties2[0])
b2 = ufloat(params2[1],uncertainties2[1])

#Halbwertszeit
#experimentell
T_s = np.log(2)/lam
T_f = np.log(2)/lam2

#theorie
T_f_th = 42.3 #s
T_s_th = 4.32 * 60 #s

#Ausgabe
print(N_R_dif)
print('N_U =', N_U_err)
print('Slow: lam =',lam,', b =', b, ', T =',T_s, ', Abw. =',(T_s_th-T_s)*100/T_s_th,'%')
print('Fast: lam =',lam2,', b =', b2, ', T =',T_f, ', Abw. =',(T_f_th-T_f)*100/T_f_th,'%')
print(unp.nominal_values(T_s), unp.std_devs(T_s))

#Plots
plt.yscale('log')
plt.xlabel(r'$t \,/\, s$')
plt.ylabel(r'$N \,/\, \frac{Imp}{15 s}$')
plt.plot(t,unp.nominal_values(N_R_dif), 'b.', label='Messwerte')
plt.plot(t[:14], unp.nominal_values(N_R_fast[:14]), 'rx' ,label = 'korrigierte Messwerte')
plt.plot(t, np.exp(f(t, unp.nominal_values(lam),unp.nominal_values(b) )), label='Ausgleichsgerade, langsamer Zerfall')
plt.plot(t[0:14], np.exp(f(t[0:14], unp.nominal_values(lam2),unp.nominal_values(b2)) ), label='Ausgleichsgerade, schneller Zerfall')
plt.errorbar(t,unp.nominal_values(N_R_dif),yerr=unp.std_devs(N_R_dif), fmt='c,',label='Messfehler')
plt.errorbar(t[:14], unp.nominal_values(N_R_fast[:14]), yerr=unp.std_devs(N_R_fast[:14]), fmt='c,')
plt.grid()
plt.legend(loc='best')
plt.savefig('build/rhodium.pdf')
plt.show()