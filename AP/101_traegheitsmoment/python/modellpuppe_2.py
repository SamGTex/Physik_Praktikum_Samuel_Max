import numpy as np
from uncertainties import ufloat

#daten allgemein
D=ufloat(0.032,0.014)
I_d=ufloat(0.0038,0.0019)

#Funktionen
def I(T):
    return T**2*D/(4*np.pi**2)
#Daten Modellpuppe
h_arm=13.7/100 #m
r_arm=0.6/100 #m
h_bein=17.2/100 #m
r_bein=0.65/100 #m
h_ober=10/100 #m
r_ober=1.95/100 #m
r_kopf=1.5/100 #m

m=0.1620 #kg
dichte=430 #kg/m^2
m_kopf=4/3 *np.pi*r_kopf**3 * dichte 
m_ober=np.pi*r_ober**2 *h_ober * dichte
m_arm=np.pi*r_arm**2 *h_arm * dichte
m_bein=np.pi*r_bein**2 *h_bein * dichte
messung, T = np.genfromtxt('data/modellpuppe2.csv', comments='#', unpack=True, delimiter=',')

#Rechnung
T_mittel=ufloat(T.mean(),T.std(ddof=1))
I_puppe2_ex = I(T_mittel) - I_d
I_puppe2_th = (2/5) * m_kopf*r_kopf**2 + (m_ober*r_ober**2)/2 + 2*m_arm*((r_arm**2)/4 + (h_arm**2)/12) + 2*m_arm*(r_ober+h_arm/2)**2 + 2*(m_bein*r_bein**2)/2 + 2*m_bein*r_bein**2
I_diff=I_puppe2_th - I_puppe2_ex

#Ausgabe
print('T_mittel =',T_mittel)
print('I_th =', I_puppe2_th)
print('I_ex =',I_puppe2_ex)
print('Abweichung:',I_diff,'(', I_diff*100/I_puppe2_th,'% )')