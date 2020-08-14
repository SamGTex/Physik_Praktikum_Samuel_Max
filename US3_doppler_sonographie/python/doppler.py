import numpy as np
#from uncertainties import ufloat
import matplotlib.pyplot as plt
#from scipy.optimize import curve_fit
#from uncertainties.unumpy import uarray
#from uncertainties import unumpy as unp
#from scipy.stats import sem

angel,  N,  f= np.genfromtxt('data/angelwithrpm.csv', delimiter=',', unpack=True)
#Grundfrequenz, schallgeschwindigkeit in verschiedenen medien
f_g = 2*10**6
c_l = 1800
c_p = 2700
angel = np.radians(angel)

#berechnung des dopplerwinkels und der frequenzverschiebung, sowie der stroemungsgeschwindigkeit
alpha = np.pi/2 - np.arcsin(np.sin(angel) * c_l/c_p)
delta_f = abs(f - f_g)
v = (c_l+c_p)/2 * delta_f/(2*f_g+np.cos(alpha))
print(delta_f[:5]/(np.cos(alpha[:5])*1000), delta_f[5:10]/(np.cos(alpha[5:10])*1000), delta_f[10:]/(np.cos(alpha[10:])*1000))
#Plots
plt.subplot(3,1,1)
plt.plot(N[:5], f[:5]/(np.cos(alpha[:5])*1000),'rx', label=r'$15\degree$')
plt.xlabel(r'$N \,/\, rpm$')
plt.ylabel(r'$\frac{ \nu}{\cos{\alpha}}\, /\, Hz$')
plt.grid()
plt.legend()
plt.subplot(3,1,2)
plt.plot(N[5:10], f[5:10]/(np.cos(alpha[5:10])*1000),'gx', label=r'$30\degree$')
plt.xlabel(r'$N \,/\, rpm$')
plt.ylabel(r'$\frac{ \nu}{\cos{\alpha}}\, /\, Hz$')
plt.legend()
plt.grid()
plt.subplot(3,1,3)
plt.plot(N[10:], f[10:]/(np.cos(alpha[10:])*1000),'bx', label=r'$45\degree$')
plt.xlabel(r'$N \,/\, rpm$')
plt.ylabel(r'$\frac{ \nu}{\cos{\alpha}}\, /\, Hz$')
plt.grid()
plt.legend()
plt.savefig('doppler.pdf')
plt.show()