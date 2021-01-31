import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

#Werte
theta, N = np.genfromtxt('data/Strontium.dat', delimiter=',', unpack=True)
Z = 38 #Ordnungszahl
t = 20 #s
alpha = 7.297352533 * 10**(-3)

#Konstanten
d = 201.4*10**(-12) #m
h = 6.626*10**(-34) #Js
c = 299792458 #m/s
R_inf = 13.6 * 1.602176634*10**(-19) #J

#Minimum und Maximum von N
N_min = np.amin(N)
N_max = np.amax(N)
index_min = np.where(N == N_min)
index_max = np.where(N == N_max)
print('index_min =',index_min)
print('index_max =',index_max)
theta_min = theta[index_min[0][0]]
theta_max = theta[index_max[0][0]]
print('min:',theta_min,N_min)
print('max:',theta_max,N_max)

#I_k
I_k_ber = N_min + (N_max-N_min)/2
print('I_k_ber =',I_k_ber)
theta_k = 11.1 #Grad (abgeschaetzt)
I_k = 120 #Imps/s (abgeschaetzt)

#Absorptionsenergie fuer K-Kante
lam_k = 2*d*np.sin(np.radians(theta_k))
E_k = h*c/lam_k
print('E_k =',E_k)

#Abschirmkonstante
sigma_k = Z - (E_k/R_inf - alpha**2 * Z**4 / 4)**(1/2)
print('sigma_k =',sigma_k)

#Plots
plt.xlabel(r'$\theta \,/\, \degree$')
plt.ylabel(r'$N \,/\, \frac{Imp}{s}$')
plt.plot(theta,N,'b.',label='Messwerte')
plt.axvline(theta_min,color='green',linestyle='--',label=r'$I_{k,min}$')
plt.axvline(theta_max,color='green',linestyle='--',label=r'$I_{k,max}$')
plt.axvline(theta_k,color='red',linestyle='--',label=r'$I_k$')
plt.grid()
plt.legend()
plt.savefig('build/strontium.pdf')
plt.show()