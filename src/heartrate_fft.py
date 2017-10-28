# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 19:23:10 2017

@author: mminestrelli
"""

import numpy as np
import matplotlib.pyplot as plt
import time
from src import video_processing_utils as vpu
from src.fft import fft

#Process video, get frames and RGB channels analize an area of squareSize and then substract the mean
#Params: videoName under path /Videos, a Location Area to analize and a squareSize

[r,g,b,f] = vpu.getFilteredRGBVectors('fierens.mp4', vpu.Location.CENTER, 30,61)


sta = time.perf_counter()
R = np.abs(np.fft.fftshift(np.fft.fft(r))) ** 2
G = np.abs(np.fft.fftshift(np.fft.fft(g))) ** 2
B = np.abs(np.fft.fftshift(np.fft.fft(b))) ** 2

end = time.perf_counter()

sta2 = time.perf_counter()

R2 = np.abs(np.fft.fftshift(fft.fft_opt(r, len(r), 1, 0))) ** 2
G2 = np.abs(np.fft.fftshift(fft.fft_opt(g, len(g), 1, 0))) ** 2
B2 = np.abs(np.fft.fftshift(fft.fft_opt(b, len(b), 1, 0))) ** 2

end2 = time.perf_counter()

sta3 = time.perf_counter()

R3 = np.abs(np.fft.fftshift(fft.fft_iter_opt(r))) ** 2
G3 = np.abs(np.fft.fftshift(fft.fft_iter_opt(g))) ** 2
B3 = np.abs(np.fft.fftshift(fft.fft_iter_opt(b))) ** 2

end3 = time.perf_counter()


print("Tiempo de corrida np.fft: {}".format(end - sta))
print("Tiempo de corrida dft: {}".format(end2 - sta2))
print("Tiempo de corrida fft_iter_opt: {}".format(end3 - sta3))


#print(np.fft.fft(r) ** 2)
#print(fft.fft_opt(r, len(r), 1, 0) ** 2)
#print(fft.fft_iter_opt(r) ** 2)

plt.plot(60 * f, R, "r")
plt.xlim(0, 200)

plt.plot(60 * f, G, "g")
plt.xlim(0, 200)

plt.plot(60 * f, B, "b")
plt.xlim(0, 200)

plt.xlabel("frecuencia [1/minuto]")
# plt.figure()
# plt.plot(60 * f, R2, "r")
# plt.xlim(0, 200)
#
# plt.plot(60 * f, G2, "g")
# plt.xlim(0, 200)
#
# plt.plot(60 * f, B2, "b")
# plt.xlim(0, 200)
#
# plt.xlabel("frecuencia 2 [1/minuto]")

plt.figure()
plt.plot(60 * f, R3, "r")
plt.xlim(0, 200)

plt.plot(60 * f, G3, "g")
plt.xlim(0, 200)

plt.plot(60 * f, B3, "b")
plt.xlim(0, 200)

plt.xlabel("frecuencia 2 [1/minuto]")

print("[Verde] Frecuencia cardíaca: ", abs(f[np.argmax(G)]) * 60, " pulsaciones por minuto")
print("[Rojo] Frecuencia cardíaca: ", abs(f[np.argmax(R)]) * 60, " pulsaciones por minuto")
print("[Azul] Frecuencia cardíaca: ", abs(f[np.argmax(B)]) * 60, " pulsaciones por minuto")
plt.show()

