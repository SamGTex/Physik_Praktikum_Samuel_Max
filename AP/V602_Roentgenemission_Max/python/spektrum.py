import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d
from scipy.signal import find_peaks
from scipy.interpolate import UnivariateSpline
import scipy.constants as cn

def f(x1,x2,y1,y2):
    a = (y2-y1)/(x2-x1)
    b = y1 - a*x1
    return a,b
def wave(l):
    d = 201.4 * 10**(-12)
    n = 1
    return 2*d*np.sin(np.radians(l)) / n 
theta, N = np.genfromtxt('data/Emissionsspektrum.dat', delimiter=',', unpack=True)

print('kb peak:',20.2,1599.0,'lambda =','1.39*10^-10m', 'E = h*c/lambda = ', '1.4282*10^-15J')
print('ka peak:',22.5,5050.0,'lambda =','1.54*10^-10m', 'E = h*c/lambda = ', '1.2887*10^-15J')
z = 29
n=1
m=2
l=3
Emax_b = 1.4282*10**(-15) #J
Emax_a = 1.2887*10**(-15) #J
EK_abs = 8987.9 * cn.e
R_inf = 13.6 * cn.e
sigma_1 = -np.sqrt(EK_abs/R_inf) + z 
sigma_2 = z - ((m/n)**2 * (z-sigma_1)**2 - Emax_a*m**2 /R_inf )**(1/2)
sigma_3 = z - ((l/n)**2 * (z-sigma_1)**2 - Emax_b*l**2 /R_inf )**(1/2)

print('abschirmkonstanten : sigma 1 ,', sigma_1, ' sigma2 ,', sigma_2, ' sigma 3 , ', sigma_3, ' und sigma gabriel', 'nan')

#beta-linie theta=x und N=y

x_max1=20.2
y_max1=1599
x1=20
y1=291
x2=20.1
y2=1127.0
a1,b1=f(x1,x2,y1,y2)
x_1=np.array([x1,x2])


#print(a1,b1)

x3=20.5
y3=1267.0
x4=20.6
y4=425.0
a2,b2=f(x3,x4,y3,y4)
x_2=np.array([x3,x4])

#alpha-linie
x_max2=22.5
y_max2=5050
x5=22.4
y5=4128.0
x6=22.3
y6=536.0
a3,b3=f(x5,x6,y5,y6)
x_3=np.array([x5,x6])

x7=22.8
y7=4097.0
x8=22.9
y8=901.0
a4,b4=f(x7,x8,y7,y8)
x_4=np.array([x7,x8])

#breite
def gerade(y,a,b):
    return (y-b)/a
x_b1 = gerade(y_max1/2,a1,b1)
x_b2 = gerade(y_max1/2,a2,b2)
x_b3 = gerade(y_max2/2,a3,b3)
x_b4 = gerade(y_max2/2,a4,b4)

#x werte der ersten halbwerts gerade
x_B1 = np.array([x_b1, x_b2])

#x werte der zweiten halbwertsgerade
x_B2 = np.array([x_b3, x_b4])
print('Halbwertsbreite links, ', abs(x_b1-x_b2))
print('Halbwertsbreite rechts, ', abs(x_b3- x_b4))


#energien berechnen
#linke (erste) energie diff
E_1 = cn.c * cn.h / wave(x_B1)
E_b = E_1[0] - E_1[1]
print('Energie diff links: ', E_b/cn.e)

#zweite (rechte) energie diff
E_2 = cn.c * cn.h / wave(x_B2)
E_a = E_2[0] - E_2[1]
print('Energie diff rechts: ', E_a/cn.e)

#Aufloesungsvermögen
A_a = Emax_a/ E_a
A_b = Emax_b/ E_b
print('Emax alpha = ', Emax_a/cn.e, 'Emax beta = ', Emax_b/cn.e)
print('Auflösungsvermögen vom linkem peak: ', A_a)
print('Auflösungsvermögen vom rechtem Peak: ', A_b)
#aussehen des plots
bbox = dict(boxstyle="round", fc="0.8")

#plot
plt.xlabel(r'$\theta \,/\, \degree$')
plt.ylabel(r'$N \,/\, \frac{Imp}{s}$')
plt.grid()
plt.plot(theta,N,'k.',label='Messwerte')
plt.plot(x_1,a1*x_1+b1,'r--',label='Näherung')
plt.plot(x_2,a2*x_2+b2,'r--')
plt.plot(x_3,a3*x_3+b3,'r--')
plt.plot(x_4,a4*x_4+b4,'r--')
plt.plot(np.array([x_b1,x_b2]),np.array([y_max1/2,y_max1/2]),'g',label='Halbwertsbreite')
plt.plot(np.array([x_b3,x_b4]),np.array([y_max2/2,y_max2/2]),'g')

plt.annotate(r'$K _\beta$', (20.1, 1599.0), (18 , 1600), bbox=bbox,arrowprops=dict(arrowstyle = "->"))
plt.annotate(r'$K _\alpha$', (22.6, 5050.0), (24 , 5000), bbox=bbox,arrowprops=dict(arrowstyle = "->"))
plt.annotate('Bremsberg',(11.1,420),xytext=(11.1,1000),bbox=bbox,arrowprops=dict(arrowstyle = "->"))
plt.legend(loc='upper center',)
plt.savefig('spektrum.pdf')
plt.show()