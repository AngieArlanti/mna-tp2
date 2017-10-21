#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scipy.signal import butter, lfilter


def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y


if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.signal import freqz

    from fft import fft

    import numpy as np
    import matplotlib.pyplot as plt
    import cv2

    cap = cv2.VideoCapture('../res/videos/2017-09-14 21.53.59.mp4')
    # cap = cv2.VideoCapture('../res/videos/alonso.MOV')

    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    r = np.zeros((1, length))
    g = np.zeros((1, length))
    b = np.zeros((1, length))

    k = 0
    while (cap.isOpened()):
        ret, frame = cap.read()

        if ret == True:
            r[0, k] = np.mean(frame[330:360, 610:640, 0])
            g[0, k] = np.mean(frame[330:360, 610:640, 1])
            b[0, k] = np.mean(frame[330:360, 610:640, 2])
        # print(k)
        else:
            break
        k = k + 1

    cap.release()
    cv2.destroyAllWindows()

    n = 1024

    f = np.linspace(-n / 2, n / 2 - 1, n) * fps / n

    r = r[0, 0:n] - np.mean(r[0, 0:n])
    g = g[0, 0:n] - np.mean(g[0, 0:n])
    b = b[0, 0:n] - np.mean(b[0, 0:n])
    R = np.abs(np.fft.fftshift(fft.fft_opt(r, len(r), 1, 0))) ** 2
    G = np.abs(np.fft.fftshift(fft.fft_opt(g, len(g), 1, 0))) ** 2
    B = np.abs(np.fft.fftshift(fft.fft_opt(b, len(b), 1, 0))) ** 2

    plt.plot(60 * f, B)
    plt.xlim(0, 200)
    plt.savefig("../out/fB.png")

    lowcut = 50
    highcut = 120


    # Filter a noisy signal.

    plt.figure(2)
    plt.clf()
    plt.plot(60 * f, B, label='Noisy signal')
    plt.xlim(0, 200)

    y = butter_bandpass_filter(b, lowcut, highcut, fps, order=6)

    RBUTTER = np.abs(np.fft.fftshift(fft.fft_opt(y, len(y), 1, 0))) ** 2

    plt.plot(60 * f, RBUTTER, label='Filtered signal (%g Hz)')
    plt.xlim(0, 200)

    plt.show()
