import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

#Werte
N_wl = 1 #W
sigma = 5.7*10**(-12) #W/cm^2*K^4
emission = 0.28
f = 0.35 #cm^2

#Funktion
def T(N_zu):
    return ((N_zu - N_wl)/(f*emission*sigma))**(1/4)

#Rechungen
#2A
N_f_20 = 4 #V
I_f_20 = 2 #A
N_zu_20 = N_f_20*I_f_20 #Leistung N_zu = U_f * I_f
T_20 = T(N_zu_20)
#2.2A
N_f_22 = 4.5 #V
I_f_22 = 2.2 #A
N_zu_22 = N_f_22*I_f_22 #Leistung N_zu = U_f * I_f
T_22 = T(N_zu_22)
#2.4A
N_f_24 = 5.5 #V
I_f_24 = 2.4 #A
N_zu_24 = N_f_24*I_f_24 #Leistung N_zu = U_f * I_f
T_24 = T(N_zu_24)


#Ausgabe
print('für 2.0A: N_zu =',N_zu_20,'und T =',T_20)
print('für 2.2A: N_zu =',N_zu_22,'und T =',T_22)
print('für 2.4A: N_zu =',N_zu_24,'und T =',T_24)