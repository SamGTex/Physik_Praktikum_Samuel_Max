import numpy as np
import matplotlib.pyplot as plt

def f(x,ak,wk):
    return ak*np.cos(wk*x)

T = np.pi
w=[]
ak=[]

for k in range(18):
    a=np.pi
    b=0
    w.append(2*np.pi*k/T)
    ak.append(4/(-4*k**2*np.pi+np.pi))

wk_np=np.array(w)
ak_np=np.array(ak)

x_np=np.linspace(0,np.pi,18)
print(ak_np)
print(wk_np)
y_np=f(x_np,ak_np,wk_np)
plt.plot(x_np,y_np)
plt.plot(np.sin(x_np))
plt.show()
#https://www.onlinemathe.de/forum/Fourier-Reihe-sinx