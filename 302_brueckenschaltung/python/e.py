import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
def g(o):
    z=(o**2-1)**2
    n=9*((1-o**2)**2 + 9*(o**2))
    return np.sqrt(z/n)
with open('daten/e.csv' ) as csvfile:
    reader=csv.reader(csvfile, delimiter=',')
    header_row=next(reader)
    f, u = [], []
    for row in reader:
        f.append(row[0])
        u.append(row[1])
    f=np.array(f,dtype=float)
    u=np.array(u,dtype=float)
    u_s=1000
    v0=160
    plt.xlabel(r'$v/v_0$')
    plt.ylabel(r'$U_{Br}/U_S$')
    R=1000
    C=993*10**(-9)
    w0=1/(R*C)
    print('w0:',w0)
    v1=w0/(2*np.pi)
    print('v0',v1)
    o=f*np.pi*2/w0
    plt.semilogx(f/v0,u/u_s,'rx',label='Messwerte')
    plt.semilogx(o,g(o),label='Theoretische Funktion')
    plt.legend()
    plt.savefig('plot_e.pdf')
    plt.show()