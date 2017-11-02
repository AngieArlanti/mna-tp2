import time

import numpy as np

from src.fft import fft
from src.utils import video_processing_utils as vpu
from src.utils.directory_utils import validateDirectories

validateDirectories()

def runBenchMark(band):
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

    return [sta, end, sta2, end2, sta3, end3, sta4, end4]

def printBenchMark(band,bandId):
    [startTimeNumpyFFT, endTimeNumpyFFT , startTimeFFTOpt, endTimeFFTOpt, startTimeIterOpt, endTimeIterOpt, startTimeDFT, endTimeDFT] = runBenchMark(band)

    print("Corriendo Benchmark para "+bandId)
    print("Tiempo de corrida DFT: {}".format(endTimeDFT-startTimeDFT))
    print("Tiempo de corrida FFT Optimizada: {}".format(endTimeFFTOpt-startTimeFFTOpt))
    print("Tiempo de corrida FFT Iterativa y Optimizada: {}".format(endTimeIterOpt-startTimeIterOpt))
    print("Tiempo de corrida FFT Numpy Library: {}\n".format(endTimeNumpyFFT-startTimeNumpyFFT))



videoName = 'fierens.mp4'
video_path = '../../res/videos/'
#Process video, get frames and RGB channels analize an area of squareSize and then substract the mean
#Params: videoName under path /Videos, a Location Area to analize and a squareSize
[r,g,b,f] = vpu.getFilteredRGBVectors(video_path+videoName, vpu.Location.CENTER, 30,60)

printBenchMark(r,"Rojo")
printBenchMark(g,"Verde")
printBenchMark(b,"Azul")

