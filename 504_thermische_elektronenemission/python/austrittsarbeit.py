import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties import unumpy as unp
from scipy.stats import sem

#Konstanten
e_0 = 1.602176634*10**(-19) #C
m_0 = 9.1093837*10**(-31) #Kg
k = 1.380649*10**(-23) #J/K
N_wl = 1 #W
sigma = 5.7*10**(-12) #W/cm^2*K^4
emission = 0.28
f = 0.35 #cm^2
h = 6.626070*10**(-34) #Js

#Funktion
def W(I_s,T):
    temp = unp.log(I_s*h**3/(4*np.pi*f*e_0*m_0*k**2*T**2))
    return -k*T*temp/e_0

#Werte
I_s_20 = ufloat(131.2,0.7)
I_s_22 = ufloat(664.8,2.2)
I_s_24 = ufloat(4.25,0.18)*10**3

T_20 = 1881.48
T_22 = 1997.89
T_24 = 2161.80

W_20 = W(I_s_20,T_20)
W_22 = W(I_s_22,T_22)
W_24 = W(I_s_24,T_24)
W = np.array([W_20,W_22,W_24])
W_mittel=np.mean(W)

#Ausgabe
print('Austrittsarbeit in eV:')
print('2.0A: ',W_20)
print('2.2A: ',W_22)
print('2.4A: ',W_24)
print('Durchschnit:', W_mittel)