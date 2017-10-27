import numpy as np
import matplotlib.pyplot as plt
from src import video_processing_utils as vpu
from src.fft import fft

#Process video, get frames and RGB channels analize an area of squareSize and then substract the mean
#Params: videoName under path /Videos, a Location Area to analize and a squareSize
[r,g,b,f] = vpu.getFilteredRGBVectors('arlanti.mp4', vpu.Location.CENTER, 30)

R = np.abs(np.fft.fftshift(fft.fft_iter_opt(r))) ** 2
G = np.abs(np.fft.fftshift(fft.fft_iter_opt(g))) ** 2
B = np.abs(np.fft.fftshift(fft.fft_iter_opt(b))) ** 2

plt.xlabel("frecuencia [1/minuto]")
plt.plot(60 * f, R, "r")
plt.xlim(0, 200)

plt.plot(60 * f, G, "g")
plt.xlim(0, 200)

plt.plot(60 * f, B, "b")
plt.xlim(0, 200)

plt.show()

print("Frecuencia cardíaca con R: ", abs(f[np.argmax(R)]) * 60, " pulsaciones por minuto")
print("Frecuencia cardíaca con G: ", abs(f[np.argmax(G)]) * 60, " pulsaciones por minuto")
print("Frecuencia cardíaca con B: ", abs(f[np.argmax(B)]) * 60, " pulsaciones por minuto")