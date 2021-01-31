import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

#funktion
def func(w,rc):
    return -np.arctan(-w*rc)

#daten einlesen
with open('data/phase.csv' ) as csvfile:
    reader=csv.reader(csvfile, delimiter=',')
    header_row=next(reader)
    f, U, a, b = [], [], [], []
    for row in reader:
        f.append(row[0])
        U.append(row[1])
        a.append(row[2])
        b.append(row[3])
    f=np.array(f,dtype=float)
    U=np.array(U,dtype=float)
    a=np.array(a,dtype=float)
    b=np.array(b,dtype=float)

#curvefit
U0=0.6
popt, pcov = curve_fit(func, f*2*np.pi, (a/b)*2*np.pi)
a1=popt[0]

#theoriewerte
R_th=11.01*10**3
C_th=93.3*10**(-9)

#plots
plt.xlabel(r'$f\, / \, Hz$')
plt.ylabel(r'$\varphi \, / \, rad$')
plt.grid()
plt.semilogx(f,(a/b)*2*np.pi,'rx',label='Messwerte')
x=np.linspace(10,30000,10000)
plt.semilogx(x,func(x*2*np.pi,a1),'b-',label='lineare Ausgleichsrechnung')
plt.semilogx(x,func(x*2*np.pi,R_th*C_th), 'g-', label='Theoriekurve')
plt.legend()
plt.savefig('plotc.pdf')
plt.show()

#fehlerausgabe
uncertainties = np.sqrt(np.diag(pcov))
print('RC =',a1,'+-',uncertainties[0])
print('Theoriewert:',11.01*1000*93.3*10**(-9))