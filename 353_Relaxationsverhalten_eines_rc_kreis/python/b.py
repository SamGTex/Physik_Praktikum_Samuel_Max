import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

#funktion
def func(w,rc):
    return 1/(np.sqrt(1+w**2*rc**2))

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
popt, pcov = curve_fit(func, f*2*np.pi, U/U0)
a1=popt[0]

#plots
plt.xlabel(r'$f\, / \, Hz$')
plt.ylabel(r'$U_c \, / \, V$')
plt.grid()
plt.semilogx(f,U/U0,'rx',label='Messwerte')
x=np.linspace(20,30000,10000)
plt.semilogx(x,func(x*2*np.pi,a1),'b-',label='lineare Ausgleichsrechnung')
plt.legend()
plt.savefig('plotb.pdf')
plt.show()

#fehlerausgabe
uncertainties = np.sqrt(np.diag(pcov))
print('RC =',-a1,'+-',uncertainties[0])
print('Theoriewert:',11.01*1000*93.3*10**(-9))