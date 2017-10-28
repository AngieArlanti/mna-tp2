import numpy as np
from src.fft import fft
from enum import Enum

class FFTMethod(Enum):
    NUMPY_FFT = 1
    DFT = 2
    FFT_OPT = 3
    FFT_ITER = 4
    FFT_ITER_OPT = 5


def getHeartRateFromBandVector(vector,f):
    return abs(f[np.argmax(vector)]) * 60

def runFFTWithMethod(FFTMethod,r,g,b,f):

    [R,G,B] = calculateFFT(FFTMethod,r,g,b)

    return [R,G,B]


def calculateFFT(FFTMethod,r,g,b):

    if FFTMethod.value <FFTMethod.FFT_ITER_OPT.value:
        FFTMethod = FFTMethod.FFT_ITER_OPT

    numpyFFT = [np.abs(np.fft.fftshift(np.fft.fft(r))) ** 2, np.abs(np.fft.fftshift(np.fft.fft(g))) ** 2,
                np.abs(np.fft.fftshift(np.fft.fft(b))) ** 2]

    DFT = [np.abs(np.fft.fftshift(fft.dft(r))) ** 2, np.abs(np.fft.fftshift(fft.dft(g))) ** 2,
               np.abs(np.fft.fftshift(fft.dft(b))) ** 2]

    FFTOpt = [np.abs(np.fft.fftshift(fft.fft_opt(r, len(r), 1, 0))) ** 2,np.abs(np.fft.fftshift(fft.fft_opt(g, len(b), 1, 0))) ** 2,
              np.abs(np.fft.fftshift(fft.fft_opt(b, len(b), 1, 0))) ** 2]

    FFTIter = [np.abs(np.fft.fftshift(fft.fft_iter(r))) ** 2, np.abs(np.fft.fftshift(fft.fft_iter(g))) ** 2,
                np.abs(np.fft.fftshift(fft.fft_iter(b))) ** 2]

    FFTIterOpt = [np.abs(np.fft.fftshift(fft.fft_iter_opt(r))) ** 2, np.abs(np.fft.fftshift(fft.fft_iter_opt(g))) ** 2,
                np.abs(np.fft.fftshift(fft.fft_iter_opt(b))) ** 2]

    choices = {FFTMethod.NUMPY_FFT:numpyFFT,FFTMethod.DFT:DFT,FFTMethod.FFT_OPT:FFTOpt,FFTMethod.FFT_ITER:FFTIter,FFTMethod.FFT_ITER_OPT:FFTIterOpt}

    return choices.get(FFTMethod)
