import csv
import matplotlib.pyplot as plt
import numpy as np

with open('data/biegung_beidseitig_rund.csv' ) as csvfile:
        reader=csv.reader(csvfile, delimiter=',')
        header_row=next(reader)
        x, D, D_0 = [], [], []
        for row in reader:
            x.append(row[0])
            D_0.append(row[1])
            D.append(row[2])
        x=np.array(x,dtype=int)
        D_0=np.array(D_0,dtype=float)
        D=np.array(D,dtype=float)
        D = 10-D
        print('D')
        print(D)
        D_0 = 10-D_0
        print('D_0')
        print(D_0)
        D_a = D-D_0
        print(D_a)
        plt.xlabel(r'$x/cm$')
        plt.ylabel(r'$D(x)$/mm')
        plt.plot(x,D_a, 'x', label='absolute Auslenkung')
        plt.legend()
        plt.grid()
        plt.savefig('plot_beidseitig_rund.pdf')
        plt.show()
        data = list(zip(x, D_0, D, D_a))
        np.savetxt('data/biegung_beidseitig_rund_data.csv', data, fmt="%1.2f", delimiter=",")
