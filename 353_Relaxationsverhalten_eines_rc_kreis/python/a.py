import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def func(T,a,b):
    return a * T + b

with open('data/entladung.csv' ) as csvfile:
    reader=csv.reader(csvfile, delimiter=',')
    header_row=next(reader)
    T, U = [], []
    for row in reader:
        T.append(row[0])
        U.append(row[1])
    T=np.array(T,dtype=float)/1000
    U=np.array(U,dtype=float)

#curvefit
U0=1
popt, pcov = curve_fit(func, T, np.log(U))
a1=popt[0]
b1=popt[1]

#plots
plt.xlabel(r'$t \, / \, ms$')
plt.ylabel(r'$\ln \left ( U_c \right ) $')
plt.grid()
plt.plot(T*1000,np.log(U),'rx',label='Messwerte')
plt.plot(T*1000,func(T,a1,b1),'b-',label='lineare Ausgleichsrechnung')
plt.legend()
plt.savefig('plota.pdf')
plt.show()

#fehlerausgabe
RC_err = (np.absolute(pcov[0][0])**0.5/a1**2)
b_err = np.absolute(pcov[1][1])**0.5
print('RC =',-1/a1,'+-',RC_err)
print('b =',b1,'+-',b_err)
print('Theoriewert:',11.01*1000*93.3*10**(-9))