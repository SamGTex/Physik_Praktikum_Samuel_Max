import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
#from scipy.interpolate import interp1d
#from scipy.signal import find_peaks
from scipy.stats import sem
import scipy.constants as cn
#from uncertainties import ufloat
#from uncertainties import unumpy as unp


#einlesen der Werte x-Ort des Messgerät, I_dun dunkelStrom, I strom mit laser
x, I_dun, I = (np.genfromtxt('data/einzelspalt.csv', delimiter=', ', unpack=True))

#CurveFit
def f(A_0, b, x):
    (A_0 * b *633*10**-9 /x) *np.sin(np.pi*b*x/633*10**-9)

#params, cov = curve_fit(f, x, I-I_dun, p0=[0.1, 50])
#print('werte der ausgleichsrechung', params)
intervall = np.linspace(0, 50, 1000)

#plotten
plt.xlabel(r'$x\, / \, mm$')
plt.ylabel(r'$I\,/\,nA$')
plt.grid()
#plt.errorbar(U, N, yerr=unp.std_devs(N_err) , fmt='r_', label='Impulse')
#plt.plot(x, I-I_dun, 'kx', label='Ausgleichsgerade')
#plt.plot(intervall, f(params[0], params[1], intervall))
plt.plot(x[:19], I[:19]-I_dun[:19], 'kx', label='Messwerte ohne Dunkelstrom')
plt.plot(x[38:], I[38:]-I_dun[38:], 'kx', label='Messwerte ohne Dunkelstrom')
plt.plot(x[19:36], I[19:36]-I_dun[19:36], 'kx', label='Messwerte ohne Dunkelstrom')
plt.legend(loc='best')

plt.show()
plt.savefig('kennlinie.pdf')