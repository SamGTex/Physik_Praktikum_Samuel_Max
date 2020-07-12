import numpy as np
import matplotlib.pyplot as plt

U_a, I_A = np.genfromtxt('data/140_grad.csv', comments='#', unpack=True, delimiter=',') #V,nA
I_A=I_A*10**(-12) #A
U_dif = (U_a[1:]-U_a[:16])
I_dif = (I_A[1:]-I_A[:16])
steigung = np.abs(I_dif/U_dif)
print(steigung*10**12) #pA/V
plt.xlabel(r'$U_A \,/\, V$')
plt.ylabel(r'$|\frac{\Delta U_A}{\Delta I_A}| \,/\, \frac{V}{A}$')
plt.grid()
plt.plot(U_a[:16],steigung,'rx')
plt.savefig('build/140_grad_dif.pdf')
plt.show()