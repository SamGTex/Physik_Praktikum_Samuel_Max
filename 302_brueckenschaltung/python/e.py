import csv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

with open('daten/e.csv' ) as csvfile:
    reader=csv.reader(csvfile, delimiter=',')
    header_row=next(reader)
    f, u = [], [],
    for row in reader:
        f.append(row[0])
        u.append(row[1])
    f=np.array(f,dtype=float)
    u=np.array(u,dtype=float)
    u_s=1
    v0=150
    #plt.xlabel(r'$f / \mathr{Hertz}, U / mV$')
    #plt.ylabel(r'$F \, / \, \mathrm{N} $')
    plt.semilogx(f/v0,u/u_s,'rx')
    plt.show()