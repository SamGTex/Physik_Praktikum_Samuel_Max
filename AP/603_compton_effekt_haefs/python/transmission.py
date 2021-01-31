import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat
from uncertainties.unumpy import uarray
from uncertainties import unumpy as unp
def f(x,a,b):
    return a*x+b

theta, N_al = np.genfromtxt('data/ComptonAl.txt', delimiter=',', unpack=True)
theta, N_o = np.genfromtxt('data/ComptonOhne.txt', delimiter=',', unpack=True)
t=200 #s
theta = np.pi * theta / 180 #rad
tau=90*10**(-6) #s

lambda1 = 2 * 201.4*10**(-12) * np.sin(theta) #pm
N_al_err = uarray(N_al,(N_al * t)**(1/2) / t)
N_o_err = uarray(N_o,(N_o * t)**(1/2) / t)
I_al = N_al_err/(1-tau*N_al_err)
I_o = N_o_err/(1-tau*N_o_err)
T = I_al/I_o

params, cov = curve_fit(f, lambda1, unp.nominal_values(T), sigma=unp.std_devs(T), p0=[100000,0.5])
uncertainties = np.sqrt(np.diag(cov))
a=ufloat(params[0],uncertainties[0])
b=ufloat(params[1],uncertainties[1])
x=np.linspace(np.min(lambda1),np.max(lambda1),100)

#Aufgabe 2.2
t=300 #s
I_0 = 2731 #Impulse
I_1 = 1180 #Impulse
I_2 = 1024 #Impulse
T_1 = I_1/I_0
T_2 = I_2/I_0

lambda_1 = (T_1-b)/a
lambda_2 = (T_2-b)/a

print('a =', a)
print('b =', b)
print('lambda1 =',lambda_1)
print('lambda2 =',lambda_2)
print('lambda_c =',lambda_2-lambda_1)

plt.xlabel(r'$\lambda \,/\, m$')
plt.ylabel(r'$T(\lambda)$')
plt.errorbar(lambda1,unp.nominal_values(T),yerr=unp.std_devs(T), fmt='r,',label='Messwerte')
plt.plot(x,f(x,params[0],params[1]),label='Lineare Ausgleichsrechnung')
plt.legend()
plt.grid()
plt.savefig('linear.pdf')
plt.show()