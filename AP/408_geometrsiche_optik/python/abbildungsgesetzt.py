import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
#from scipy.interpolate import interp1d
#from scipy.signal import find_peaks
from scipy import stats
from scipy.stats import sem
import scipy.constants as cn
from uncertainties import ufloat
#from uncertainties import unumpy as unp
b, g, B = (np.genfromtxt('data/abbildungsgesetzt.csv', delimiter=', ', unpack=True))
G = 3
def schnittpunkt(g1,b1,g2,b2):
    t = b2*(g1-g2)/(g1*b2-g2*b1)
    s_x = g1-t*g1
    s_y = t*b1
    return (s_x,s_y)
s_x = np.array([])
s_y = np.array([])
n = g.size
for i in range(0,n):
    # Alle Schnittpunkte der i-ten Linie mit allen nachfolgenden Linien
    s_x_i,s_y_i = schnittpunkt(g[i+1:n],b[i+1:n],g[i],b[i])
    s_x = np.append(s_x,s_x_i)
    s_y = np.append(s_y,s_y_i)

V = B/G
V_mean = ufloat( np.mean(V), stats.sem(V))
V_2 = b/g 
V_2_mean = ufloat(np.mean(V_2), stats.sem(V_2))
print('Abbildungsmassstab V: ', V_mean)
print('Abbildungsmassstab V_2', V_2_mean)
print('Abbweichung der Abbildungsmasstäbe :' , np.abs(V_mean-V_2_mean))
c = 1/b + 1/g
#print(c)
f = 1/c
print(f)
print('Mittelwert der Brennweiten', np.mean(f) , stats.sem(f))
f_mean = ufloat(np.mean(f), stats.sem(f))
print('Abbweichung ', 15- f_mean)
b_plot = np.array([0, b])
g_plot = np.array([g, 0])

s_x_mean = ufloat(np.mean(s_x),stats.sem(s_x))
s_y_mean = ufloat(np.mean(s_y),stats.sem(s_y))
print('Schwerppunkt der Brennweiten', s_x_mean, s_y_mean)
print('Abbweichung der Schwerpunkte ', 15- s_x_mean, 15- s_y_mean)

for i in range(0,g.size):
    plt.plot([g[i],0],[0,b[i]], 'k-', linewidth=0.5)

plt.plot(s_x,s_y, 'r.', markersize=3.5, markeredgewidth=0, label="Schnittpunkte")
plt.errorbar(s_x_mean.n,s_y_mean.n, yerr=s_y_mean.s, xerr=s_x_mean.s, fmt='go', markersize=5, label="Schwerpunkt der Schnittpunkte")

plt.xlabel(r'$g \./\. cm$')
plt.ylabel(r'$b\./\. cm$')
plt.legend()
plt.grid()
plt.savefig('brennweite.pdf')
plt.show()