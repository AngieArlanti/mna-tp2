import numpy as np
import matplotlib.pyplot as plt
from src.fft import fft
from src.utils import video_processing_utils as vpu
from src import comparation_methods as cmp
import cv2

video_path = '../../res/videos/'
video_format = '.mp4'

# without LED

videos = vpu.get_no_led_videos()

no_led_freqs = []

for v in videos:

    [r, g, b, f] = vpu.getFilteredRGBVectors(video_path + v[0] + '-' + v[1] + '-' + v[2] + video_format, vpu.Location.CENTER, 30, 61)
    R = np.abs(np.fft.fftshift(np.fft.fft(r))) ** 2
    G = np.abs(np.fft.fftshift(np.fft.fft(g))) ** 2
    B = np.abs(np.fft.fftshift(np.fft.fft(b))) ** 2
    no_led_freqs.append([abs(f[np.argmax(R)]) * 60, abs(f[np.argmax(G)]) * 60, abs(f[np.argmax(B)]) * 60])


# with LED

videos = vpu.get_led_videos()

led_freqs = []

for v in videos:

    [r, g, b, f] = vpu.getFilteredRGBVectors(video_path + v[0] + '-' + v[1] + '-' + v[2] + video_format, vpu.Location.CENTER, 30, 61)
    R = np.abs(np.fft.fftshift(np.fft.fft(r))) ** 2
    G = np.abs(np.fft.fftshift(np.fft.fft(g))) ** 2
    B = np.abs(np.fft.fftshift(np.fft.fft(b))) ** 2
    led_freqs.append([abs(f[np.argmax(R)]) * 60, abs(f[np.argmax(G)]) * 60, abs(f[np.argmax(B)]) * 60])



print(no_led_freqs)

no_led_blues = []
for f in no_led_freqs:
    no_led_blues.append(f[2])


print(no_led_blues)

led_blues = []
for f in no_led_freqs:
    led_blues.append(f[2])

# cmp.bland_altman(no_led_blues, led_blues)
