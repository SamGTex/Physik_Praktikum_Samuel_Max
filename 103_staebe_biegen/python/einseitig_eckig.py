import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import sem
from uncertainties import ufloat

d_a = np.array([10.5, 10.3, 10.3, 10.5, 10.4, 10.3, 10.3, 10.0, 10.0, 10.1])
d_b = np.array([10.3, 10.2, 10.1, 10.1, 10.1, 10.0, 10.1, 10.0, 10.1, 10.2])
da = np.mean(d_a)
db = np.mean(d_b)
err_da = sem(d_a)
err_db = sem(d_b)
print('Mittelwert von a ist : ' ,da,'Fehler von a: ', err_da )
print('Mittelwert von b ist : ' ,db,'Fehler von b: ', err_db )
a = ufloat(da, err_da)
b = ufloat(db, err_db)
a = a / 1000
b = b/ 1000
L=49 / 100
F=(18.9 + 520.9 + 1171.8)/1000 * 9.81
I = b*a**3 / 12
V = a * b * L * 100**3
Dichte = (455.1) / V
print('Volumen = ', V, 'Dichte = ', Dichte)
print('I= ',I)
def D_Theorie(x,E):
    return F/(2* E * 9.14*10**-10) * x

def D_fit(x,E):
    return D_Theorie(x,E)

# Daten einlesen
x,D0,DM = np.genfromtxt('data/biegung_einseitig_eckig.csv',delimiter=',',unpack=True)

#Berechnungen
x = x*10**(-3) #in meter
D0 = D0*10**(-3) #in meter
DM = DM*10**(-3) #meter
D= D0-DM #meter 
         
X = 0.446*x**2 - (x**3)/3 
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
plt.savefig('plot_einseitig_eckig.pdf')

print('E2:',E*10**(-9))
print('Fehler von E2',E_err*10**(-9))
#with open('data/biegung_einseitig_eckig.csv' ) as csvfile:
        #reader=csv.reader(csvfile, delimiter=',')
        #header_row=next(reader)
        #x, D_0, D = [], [], []
        #for row in reader:
        #    x.append(row[0])
        #    D_0.append(row[1])
        #    D.append(row[2])
        #x=np.array(x,dtype=int)
        #D_0=np.array(D_0,dtype=float)
        #D=np.array(D,dtype=float)
#
#
        #D = 10-D
        #D_0 = 10-D_0
        #D_a = D-D_0
#
#
        #d_a = np.array([10.5, 10.3, 10.3, 10.5, 10.4, 10.3, 10.3, 10.0, 10.0, 10.1])
        #d_b = np.array([10.3, 10.2, 10.1, 10.1, 10.1, 10.0, 10.1, 10.0, 10.1, 10.2])
        #da = np.mean(d_a)
        #db = np.mean(d_b)
        #err_da = sem(d_a)
        #err_db = sem(d_b)
        #print('Mittelwert von a ist : ' ,da,'Fehler von a: ', err_da )
        #print('Mittelwert von b ist : ' ,db,'Fehler von b: ', err_db )
        #a = ufloat(da, err_da)
        #b = ufloat(db, err_db)
#
        #L=49
        #F=(18.9 + 520.9 + 1171.8)/1000 * 9.81
        #I = b*a**3 / 12
#
        #def f(x):
        #    return(L*(x**2)-(x**3)/3)
#
        #def curve(x, E):
        #    return F /(2*E*I) * x
        #
        #X = f(x)
        #X = np.array(X)
        #x1 = np.linspace(np.min(x), np.max(x), 1000)
        #
        ##curvefit
        #params, pcov = curve_fit(curve, X, D_a)
        #E = params[0]
        #E = np.array(E)
        #print('E',E)
#
        #plt.xlabel(r'$Lx^2 - x^3/3\,\,/cm$')
        #plt.ylabel(r'$D(x)\,\,/mm$')
        #plt.plot(f(x),D_a, 'x', label='absolute Auslenkung')
        #plt.plot(f(x1), curve(f(x1), E), 'b-', label='lineare Ausgleichsrechung')
        #plt.legend()
        #plt.grid()
        #plt.savefig('plot_einseitig_eckig.pdf')
        #plt.show()
        #data = list(zip(x, D_0, D, D_a))
        #np.savetxt('data/biegung_einseitig_eckig_data.csv', data, fmt="%1.2f", delimiter=",")

