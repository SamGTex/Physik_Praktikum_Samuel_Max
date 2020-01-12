import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import sem
from uncertainties import ufloat

d_a = np.array([10.0, 10.0, 9.9, 9.9, 10.0, 9.9, 10.0, 9.9, 10.0, 10.0])
da = np.mean(d_a)
err_da = sem(d_a)
print('Mittelwert von a ist : ' ,da,'Fehler von a: ', err_da )
a = ufloat(da, err_da)

a = (a/2) / 1000
a_cm = a * 100
L=49
V = np.pi * a_cm**2 * 55
Dichte = 360.4 / V
print('Volumen = ', V, 'Dichte = ', Dichte)
F=(18.9 + 520.9 + 1171.8)/1000 * 9.81
I = np.pi*a**4 / 4 
print('I= ',I)

def D_Theorie(x,E):
    return F/(2* E * 4.831*10**-10) * x

def D_fit(x,E):
    return D_Theorie(x,E)

# Daten einlesen
x,DM,D0 = np.genfromtxt('data/biegung_einseitig_rund.csv',delimiter=',',unpack=True)
#Berechnungen
x = x*10**(-3) #in meter
D0 = (D0)*10**(-3) #in meter
DM = (DM)*10**(-3) #meter
D= D0 - DM #meter
D = D[1::] 
print(D)
        
X = 0.49*x**2 - (x**3)/3 
X = X[1::]
print(X)
# Ausgleichskurve berechnen
params,pcov = curve_fit(D_fit,X,D)
E = params[0]

#Fehler berechnen
E_err = np.absolute(pcov[0][0])**0.5


# Plot der Ausgleichskurve
x_linspace = np.linspace(np.min(X),np.max(X),100)
plt.plot(x_linspace, D_fit(x_linspace,*params)*10**3, 'k-', label='Ausgleichsgerade')
# Plot der Daten
plt.plot(X, D*10**3, 'ro', label='Auslenkung')

# Achsenbeschriftung
plt.xlabel(r'$Lx^2 - \frac{x^3}{3} \:/\: m^3$')
plt.ylabel(r'$D \:/\: mm$')

# in matplotlibrc leider (noch) nicht möglich
plt.legend(loc='best')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.grid(True,which="both", linestyle='--')

# Speicherort
plt.savefig('plot_einseitig_rund.pdf')

print('E2:',E*10**(-9))
print('Fehler von E2',E_err*10**(-9))


#with open('data/biegung_einseitig_rund.csv' ) as csvfile:
        #reader=csv.reader(csvfile, delimiter=',')
        #header_row=next(reader)
        #x, D, D_0 = [], [], []
        #for row in reader:
        #    x.append(row[0])
        #    D.append(row[1])
        #    D_0.append(row[2])
        #x=np.array(x,dtype=int)
        #D_0=np.array(D_0,dtype=float)
        #D=np.array(D,dtype=float)
        #D = 10-D
        #D_0 = 10-D_0
        #D_a = D-D_0
        #L=49
        #def f(x):
        #    return(L*(x**2)-(x**3)/3)
        #plt.xlabel(r'$Lx^2 - x^3/3 \,\, /cm$')
        #plt.ylabel(r'$D(x) \,\, /mm$')
        #plt.plot(f(x),D_a, 'x', label='absolute Auslenkung')
        #plt.legend()
        #plt.grid()
        #plt.savefig('plot_einseitig_rund.pdf')
        #plt.show()
        #
data = list(zip(x, D0, DM, D))
np.savetxt('data/biegung_einseitig_rund_data.csv', data, fmt="%1.2f", delimiter=",")
        #with open('data/biegung_einseitig_rund_data.csv', mode='w') as csvfile:
        #    fieldnames = ['x', 'D_0', 'D', 'D_a']
        #    writer = csv.writer(csvfile)
        #    list(zip())
        #    writer.writerow(x)
        #    writer.writerow(D_0)
        #    writer.writerow(D)
        #    writer.writerow(D_a)




        
