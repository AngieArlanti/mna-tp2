import time

import numpy as np

from src.fft import fft
from src.utils import video_processing_utils as vpu

#Process video, get frames and RGB channels analize an area of squareSize and then substract the mean
#Params: videoName under path /Videos, a Location Area to analize and a squareSize
[r,g,b,f] = vpu.getFilteredRGBVectors('fierens.mp4', vpu.Location.CENTER, 30,60)

sta = time.perf_counter()
G = np.abs(np.fft.fftshift(np.fft.fft(g))) ** 2
end = time.perf_counter()

sta2 = time.perf_counter()
G2 = np.abs(np.fft.fftshift(fft.fft_opt(g, len(g), 1, 0))) ** 2
end2 = time.perf_counter()

sta3 = time.perf_counter()
G3 = np.abs(np.fft.fftshift(fft.fft_iter_opt(g))) ** 2
end3 = time.perf_counter()

sta4 = time.perf_counter()
G4 = np.abs(np.fft.fftshift(fft.dft(g))) ** 2
end4 = time.perf_counter()

print("Tiempo de corrida DFT: {}".format(end4 - sta4))
print("Tiempo de corrida FFT Optimizada: {}".format(end2 - sta2))
print("Tiempo de corrida FFT Iterativa y Optimizada: {}".format(end3 - sta3))
print("Tiempo de corrida FFT Numpy Library: {}".format(end - sta))
