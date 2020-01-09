import csv
import matplotlib.pyplot as plt
import numpy as np

with open('data/biegung_einseitig_rund.csv' ) as csvfile:
        reader=csv.reader(csvfile, delimiter=',')
        header_row=next(reader)
        x, D, D_0 = [], [], []
        for row in reader:
            x.append(row[0])
            D.append(row[1])
            D_0.append(row[2])
        x=np.array(x,dtype=int)
        D_0=np.array(D_0,dtype=float)
        D=np.array(D,dtype=float)
        D = 10-D
        D_0 = 10-D_0
        D_a = D-D_0
        L=49
        def f(x):
            return(L*(x**2)-(x**3)/3)
        plt.xlabel(r'$Lx^2 - x^3/3 \,\, /cm$')
        plt.ylabel(r'$D(x) \,\, /mm$')
        plt.plot(f(x),D_a, 'x', label='absolute Auslenkung')
        plt.legend()
        plt.grid()
        plt.savefig('plot_einseitig_rund.pdf')
        plt.show()

        data = list(zip(x, D_0, D, D_a))
        np.savetxt('data/biegung_einseitig_rund_data.csv', data, fmt="%1.2f", delimiter=",")
        #with open('data/biegung_einseitig_rund_data.csv', mode='w') as csvfile:
        #    fieldnames = ['x', 'D_0', 'D', 'D_a']
        #    writer = csv.writer(csvfile)
        #    list(zip())
        #    writer.writerow(x)
        #    writer.writerow(D_0)
        #    writer.writerow(D)
        #    writer.writerow(D_a)




        
