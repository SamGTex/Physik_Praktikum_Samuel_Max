import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d
from scipy.signal import find_peaks
from scipy.interpolate import UnivariateSpline

def f(x1,x2,y1,y2):
    a = (y2-y1)/(x2-x1)
    b = y1 - a*x1
    return a,b

theta, N = np.genfromtxt('data/Emissionsspektrum.dat', delimiter=',', unpack=True)

#Nullebene
ground = np.amin(N)
lin_ebene = np.linspace(np.min(theta),np.max(theta),1000)
print('Ground (kleinster Messwert): N =',ground)

print('Peak1 (an Nullebene angepasst):',20.2,1599.0-ground,',lam =','1.39*10^-10', ',E = h*c/lam = ', '1.4282*10^-15')
print('Peak2 (an Nullebene angepasst):',22.5,5050.0-ground,',lam =','1.54*10^-10', ',E = h*c/lam = ', '1.2887*10^-15')

E_b_max = 1.4282*10**(-15) #J
E_a_max = 1.2887*10**(-15) #J

#beta-linie theta=x und N=y
x_max1=20.2
y_max1=1599-ground
x1=20
y1=291
x2=20.1
y2=1127.0
a1,b1=f(x1,x2,y1,y2)
lin1=np.array([x1,x2])

x3=20.5
y3=1267.0
x4=20.6
y4=425.0
a2,b2=f(x3,x4,y3,y4)
lin2=np.array([x3,x4])

#alpha-linie
x_max2=22.5
y_max2=5050-ground
x5=22.4
y5=4128.0
x6=22.3
y6=536.0
a3,b3=f(x5,x6,y5,y6)
lin3=np.array([x5,x6])

x7=22.8
y7=4097.0
x8=22.9
y8=901.0
a4,b4=f(x7,x8,y7,y8)
lin4=np.array([x7,x8])

#breite
def gerade(y,a,b):
    return (y-b)/a
xb1 = gerade(y_max1/2,a1,b1)
xb2 = gerade(y_max1/2,a2,b2)
xb3 = gerade(y_max2/2,a3,b3)
xb4 = gerade(y_max2/2,a4,b4)

d = 201.4*10**(-12) #m
h = 6.626*10**(-34) #Js
c = 299792458 #m/s

lam_beta_2 = 2*d*np.sin(np.radians(xb2))
lam_beta_1 = 2*d*np.sin(np.radians(xb1))
lam_alpha_2 = 2*d*np.sin(np.radians(xb4))
lam_alpha_1 = 2*d*np.sin(np.radians(xb3))
E_beta = h*c/lam_beta_1 - h*c/lam_beta_2
E_alpha = h*c/lam_alpha_1 - h*c/lam_alpha_2
print('beta: theta =',xb1,',',xb2,',delta_E =',E_beta)
print('alpha: theta =',xb3,',',xb4,',delta_E =',E_alpha)

#auflösungsvermögen
print('beta: A = E_K/E_FWHM =', E_b_max/E_beta)
print('alpha: A = E_K/E_FWHM =',E_a_max/E_alpha)

#Abschirmkonstante
R_inf = 13.6 * 1.602176634*10**(-19) #J
E_abs = 8.9789 * 1000 * 1.602176634*10**(-19) #J
z = 29
n=1
m=2
l=3

sig1 = z - (E_abs/R_inf)**(1/2)
sig2 = z - ((m/n)**2 * (z-sig1)**2 - E_a_max*m**2 /R_inf )**(1/2)
sig3 = z - ((l/n)**2 * (z-sig1)**2 - E_b_max*l**2 /R_inf )**(1/2)
print('sigma_1 =',sig1)
print('sigma_2 =',sig2)
print('sigma_3 =',sig3)

#plot
plt.xlabel(r'$\theta \,/\, \degree$')
plt.ylabel(r'$N \,/\, \frac{Imp}{s}$')
plt.plot(lin_ebene,ground+lin_ebene*0,linestyle=':' ,color='black', label='Nullebene')
plt.plot(theta,N,'b.',label='Messwerte')
plt.plot(lin1,a1*lin1+b1,color='orangered',label='Näherung')
plt.plot(lin2,a2*lin2+b2,color='orangered')
plt.plot(lin3,a3*lin3+b3,color='orangered')
plt.plot(lin4,a4*lin4+b4,color='orangered')
plt.plot(np.array([xb1,xb2]),np.array([y_max1/2,y_max1/2]),'k',label='Halbwertsbreite')
plt.plot(np.array([xb3,xb4]),np.array([y_max2/2,y_max2/2]),'k')

plt.axvline(20.2,color='red',linestyle='--',label=r'$K_\beta$')
plt.axvline(22.5,color='green',linestyle='--',label=r'$K_\alpha$')
plt.annotate('Bremsberg',(11.1,420),xytext=(15,1000),arrowprops=dict(facecolor='black',shrink=0.05))
plt.legend()
plt.savefig('build/plot.pdf')
plt.show()