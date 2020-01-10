import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import sem
from uncertainties import ufloat


with open('data/biegung_einseitig_eckig.csv' ) as csvfile:
        reader=csv.reader(csvfile, delimiter=',')
        header_row=next(reader)
        x, D_0, D = [], [], []
        for row in reader:
            x.append(row[0])
            D_0.append(row[1])
            D.append(row[2])
        x=np.array(x,dtype=int)
        D_0=np.array(D_0,dtype=float)
        D=np.array(D,dtype=float)


        D = 10-D
        D_0 = 10-D_0
        D_a = D-D_0


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

        L=49
        F=(18.9 + 520.9 + 1171.8)/1000 * 9.81
        I = b*a**3 / 12

        def f(x):
            return(L*(x**2)-(x**3)/3)

        def curve(x, E):
            return F /(2*E*I) * x
        
        x1 = np.linspace(np.min(x), np.max(x), 1000)
        
        #curvefit
        params, pcov = curve_fit(curve, f(x), D_a)
        E = params[0]
        print('E',E)

        plt.xlabel(r'$Lx^2 - x^3/3\,\,/cm$')
        plt.ylabel(r'$D(x)\,\,/mm$')
        plt.plot(f(x),D_a, 'x', label='absolute Auslenkung')
        plt.plot(f(x1), curve(f(x1), E), 'b-', label='lineare Ausgleichsrechung')
        plt.legend()
        plt.grid()
        plt.savefig('plot_einseitig_eckig.pdf')
        plt.show()
        data = list(zip(x, D_0, D, D_a))
        np.savetxt('data/biegung_einseitig_eckig_data.csv', data, fmt="%1.2f", delimiter=",")

