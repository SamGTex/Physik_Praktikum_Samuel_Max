import numpy as np

T = np.pi
for k in range(18):

    w=2*np.pi*k/T
    a=np.pi
    b=0

    obere_1 = 2/T * (np.sign(np.sin(a)) * (w * np.sin(a) * np.sin(w * a) 
    + np.cos(a) * np.cos(w * a))) / (w**2 - 1)

    untere_1 = 2/T * (np.sign(np.sin(b)) * (w * np.sin(b) * np.sin(w * b) 
    + np.cos(b) * np.cos(w * b))) / (w**2 - 1)

    print('w:',w)
    print('A_1:',obere_1-untere_1)
    print('A_2:',4/(-4*k**2*np.pi+np.pi))

#https://www.onlinemathe.de/forum/Fourier-Reihe-sinx