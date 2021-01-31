import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

with open('data/long.csv' ) as csvfile:
    reader=csv.reader(csvfile, delimiter=',')
    header_row=next(reader)
    x, B = [], []
    for row in reader:
        x.append(row[0])
        B.append(row[1])
    x=np.array(x,dtype=float)
    B=np.array(B,dtype=float)
    plt.xlabel(r'$x/cm$')
    plt.ylabel(r'$B/mT$')
    plt.plot(x,B, 'x')
    plt.legend()
    plt.grid()
    plt.savefig('plot_e.pdf')
    plt.show()

