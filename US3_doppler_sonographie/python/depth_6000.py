import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
#from uncertainties.unumpy import uarray
#from uncertainties import unumpy as unp
#from scipy.stats import sem

depht, I, f= np.genfromtxt('data/6000.csv', delimiter=',', unpack=True)

#Einstellungen am messgerät und schallgeschwindigkeit in verschiedenen medien
N = 6000
angle = np.radians(15)
l = 0.0307
c_p = 2700
t_in_prism = l/c_p
c_l = 1800

#funktion zur berechung der Messtiefe im schlauch
def depth_in_mm(depth):
    depth = depth*10**-6
    depth = depth-t_in_prism
    return c_l*depth

def func(a,x):
    return a*x+100

def func_2(a,b, x):
    return a*x+b

prms, pcov = curve_fit(func, depth_in_mm(depht), I)
x = np.linspace(0.002,0.014,10000)
#print(depth_in_mm(depht))
print(prms[0])
print(pcov)
plt.subplot(2,1,1)
plt.plot(depth_in_mm(depht)*1000,I,'rx', label='Streuintensität')
#plt.plot(x*1000, func(prms[0], x), 'b-', label='Lineare Ausgleichsrechnung')
plt.xlabel(r'$Messtiefe \,/\, mm$')
plt.ylabel(r'$ I\,/\, 10^3 \frac{V^2}{s}$')
plt.grid()
plt.legend()
#plt.savefig('depth_3880_I.pdf')
#plt.show()


prms_2, pcov_2 = curve_fit(func_2, depth_in_mm(depht), f)
plt.subplot(212)
plt.plot(depth_in_mm(depht)*1000,f,'kx', label='maximale Frequenz')
#plt.plot(x, func_2(prms_2[0],prms_2[1], x), 'g-', label='Lineare Ausgleichsrechnung')
plt.xlabel(r'$Messtiefe \,/\, mm$')
plt.ylabel(r'$ f\,/\, Hz$')
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig('depth_6000.pdf')
plt.show()
