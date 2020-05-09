import numpy as np

alpha = 7.297*10**(-3)
R_inf = 13.6 #eV
d = 201.4*10**(-12) #m
h = 4.136*10**(-15) #eVs
c = 299792458 #m/s

#Zn
Z_zn = 30
E_zn = 9.6586 *1000 #eV
lam_zn = h*c/E_zn
theta_zn = np.arcsin(lam_zn/(2*d))
sig_zn = Z_zn - np.sqrt(E_zn/R_inf - alpha**2 * Z_zn**4 / 4)

print('Zn:')
print('Z =',Z_zn)
print('E_K =',E_zn)
print('lam =',lam_zn)
print('theta =',np.degrees(theta_zn))
print('sigma =',sig_zn)

#Ge
Z_Ge = 32
E_Ge = 11.1031 *1000 #eV
lam_Ge = h*c/E_Ge
theta_Ge = np.arcsin(lam_Ge/(2*d))
sig_Ge = Z_Ge - np.sqrt(E_Ge/R_inf - alpha**2 * Z_Ge**4 / 4)

print('----------------------------')
print('Ge:')
print('Z =',Z_Ge)
print('E_K =',E_Ge)
print('lam =',lam_Ge)
print('theta =',np.degrees(theta_Ge))
print('sigma =',sig_Ge)

#Br
Z_Br = 35
E_Br = 13.4737 *1000 #eV
lam_Br = h*c/E_Br
theta_Br = np.arcsin(lam_Br/(2*d))
sig_Br = Z_Br - np.sqrt(E_Br/R_inf - alpha**2 * Z_Br**4 / 4)

print('----------------------------')
print('Br:')
print('Z =',Z_Br)
print('E_K =',E_Br)
print('lam =',lam_Br)
print('theta =',np.degrees(theta_Br))
print('sigma =',sig_Br)

#Rb
Z_Rb = 37
E_Rb = 15.1997 *1000 #eV
lam_Rb = h*c/E_Rb
theta_Rb = np.arcsin(lam_Rb/(2*d))
sig_Rb = Z_Rb - np.sqrt(E_Rb/R_inf - alpha**2 * Z_Rb**4 / 4)

print('----------------------------')
print('Rb:')
print('Z =',Z_Rb)
print('E_K =',E_Rb)
print('lam =',lam_Rb)
print('theta =',np.degrees(theta_Rb))
print('sigma =',sig_Rb)


#Sr
Z_Sr = 38   
E_Sr = 16.1046 *1000 #eV
lam_Sr = h*c/E_Sr
theta_Sr = np.arcsin(lam_Sr/(2*d))
sig_Sr = Z_Sr - np.sqrt(E_Sr/R_inf - alpha**2 * Z_Sr**4 / 4)

print('----------------------------')
print('Sr:')
print('Z =',Z_Sr)
print('E_K =',E_Sr)
print('lam =',lam_Sr)
print('theta =',np.degrees(theta_Sr))
print('sigma =',sig_Sr)


#Zr
Z_Zr = 40
E_Zr = 17.9976 *1000 #eV
lam_Zr = h*c/E_Zr
theta_Zr = np.arcsin(lam_Zr/(2*d))
sig_Zr = Z_Zr - np.sqrt(E_Zr/R_inf - alpha**2 * Z_Zr**4 / 4)

print('----------------------------')
print('Zr:')
print('Z =',Z_Zr)
print('E_K =',E_Zr)
print('lam =',lam_Zr)
print('theta =',np.degrees(theta_Zr))
print('sigma =',sig_Zr)