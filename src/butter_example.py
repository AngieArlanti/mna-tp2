#!/usr/bin/env python
# -*- coding: utf-8 -*-

from passband_filter import PBFilter

if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    from fft import fft
    import cv2

    # cap = cv2.VideoCapture('../res/videos/2017-09-14 21.53.59.mp4')
    cap = cv2.VideoCapture('../res/videos/alonso.mp4')

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

        if ret:
            r[0, k] = np.mean(frame[330:360, 610:640, 0])
            g[0, k] = np.mean(frame[330:360, 610:640, 1])
            b[0, k] = np.mean(frame[330:360, 610:640, 2])
        else:
            break
        k = k + 1

    cap.release()
    cv2.destroyAllWindows()

    n = 1024

    f = np.linspace(-n / 2, n / 2 - 1, n) * fps / n

    # Normalize
    r = r[0, 0:n] - np.mean(r[0, 0:n])
    g = g[0, 0:n] - np.mean(g[0, 0:n])
    b = b[0, 0:n] - np.mean(b[0, 0:n])

    R = np.abs(np.fft.fftshift(fft.fft_opt(r, len(r), 1, 0))) ** 2
    G = np.abs(np.fft.fftshift(fft.fft_opt(g, len(g), 1, 0))) ** 2
    B = np.abs(np.fft.fftshift(fft.fft_opt(b, len(b), 1, 0))) ** 2

    # plt.plot(60 * f, B)
    # plt.xlim(0, 200)
    # plt.savefig("../out/fB.png")

    # Filter a noisy signal.

    plt.figure(2)
    plt.clf()
    plt.plot(60 * f, B, label='Noisy signal')
    plt.xlim(0, 250)

    b_butter = PBFilter().filter(b, fps)

    # Cut the initial stabilization time (1 second). Nuestro pico cerca de 0.
    # ver http://www.ignaciomellado.es/blog/Measuring-heart-rate-with-a-smartphone-camera
    cut_frame_index = np.floor(fps * 1 + 1).astype(int)

    b_stable = np.array(b_butter[cut_frame_index: n])

    zeros = np.zeros(31)

    b_stable = np.append(zeros, b_stable)

    print(b_stable)

    B_butter = np.abs(np.fft.fftshift(fft.fft_opt(b_stable, len(b_stable), 1, 0))) ** 2

    plt.plot(60 * f, B_butter, label='Filtered signal (%g Hz)')
    plt.xlim(0, 250)

    plt.show()
