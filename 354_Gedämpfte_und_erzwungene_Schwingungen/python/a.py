import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def func(A_0,mu,t):
    return A_0*math.exp**(-2*np.pi*mu*t)

t, U =np.genfromtxt('python/data/a.csv', delimiter=',', unpack=True)

plt.xlabel(r'$t \, / \, ms$')
plt.ylabel(r'$\ln \left ( U_c \right ) $')
plt.grid()
plt.semilogx(t, U,'rx', label='Messwerte')
plt.plot(t,func(A_0,mu,t),'b-',label='lineare Ausgleichsrechnung')
plt.legend()
plt.savefig('plota.pdf')
plt.show()
#with open('data/a.csv' ) as csvfile:
#    reader=csv.reader(csvfile, delimiter=',')
#    header_row=next(reader)
#    t, U = [], []
#    for row in reader:
#        t.append(row[0])
#        U.append(row[1])
#    t=np.array(t,dtype=float)/1000
#    U=np.array(U,dtype=float)


popt, pcov = curve_fit(func, t, U)
a1=popt[0]

#
##plots
#plt.xlabel(r'$t \, / \, ms$')
#plt.ylabel(r'$\ln \left ( U_c \right ) $')
#plt.grid()
#plt.plot(t*1000,np.log(U),'rx',label='Messwerte')

#plt.legend()
#plt.savefig('plota.pdf')
#plt.show()
#
##fehlerausgabe
#RC_err = (np.absolute(pcov[0][0])**0.5/a1**2)
#b_err = np.absolute(pcov[1][1])**0.5
print('RC =',-1/a1,'+-',RC_err)
print('b =',b1,'+-',b_err)
#print('Theoriewert:',11.01*1000*93.3*10**(-9))