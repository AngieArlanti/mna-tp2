import numpy as np
import matplotlib.pyplot as plt
import time
from math import pi, cos, sin, floor

def x_e(k, x, N):
    val = x[k] + x[k + N//2]
    return val

def x_d(k, x, N):
    val = (x[k] - x[k + N//2]) * w(k,N) #este valor tendria que estar pre-calculado y sacarlo de un vector W
    return val

def w(k,N):
    y = (2*pi)/N
  #  print(y)
    val = cos(y*k) - 1j*sin(y*k)
    return val

def calculateK(i):
    k = 0
    if i > 0:
        k = floor(i/2)
    return k

def fft1(vect):
    N = len(vect) #size de vect
    a = 3 #N=2^a

    while a > 0:
        s = []
        for i in range(N):
            #calcular k
            k = calculateK(i)
            if i % 2 == 0 :
                val = x_e(k,vect,N)
            else:
                val = x_d(k,vect,N)
            s.append(val)
        a -= 1
        vect = np.around(s, decimals=3)
    return np.around(s, decimals=3)

if __name__ == "__main__":

    #f = np.linspace(-n/2,n/2-1,n)
    r = [1,1,1,1,0,0,0,0]

    sta = time.perf_counter()
    l= np.fft.fft(r)
    end = time.perf_counter()
    print("tiempo de corrida np.fft.fft: {}".format(end - sta))
    print(l)

    sta = time.perf_counter()
    l= fft1(r)
    end = time.perf_counter()
    print("tiempo de corrida fft1: {}".format(end - sta))
    print(l)


#Test W
    # print(w(0,8))
    # print(w(1,8))
    # print(w(2,8))
    # print(w(3,8))

#Test k
    # print(calculateK(0,8))
    # print(calculateK(1, 8))
    # print(calculateK(2, 8))
    # print(calculateK(3, 8))
    # print(calculateK(4, 8))
    # print(calculateK(5, 8))
    # print(calculateK(6, 8))
    # print(calculateK(7, 8))



# R = np.abs(np.fft.fftshift(np.fft.fft(r)))**2
# plt.plot(60*f,R)
# plt.xlim(0,200)
# plt.xlabel("frecuencia [1/minuto]")
#
#
# plt.savefig('res.png')