import numpy as np
import matplotlib.pyplot as plt
from src.fft import fft
from src.utils import video_processing_utils as vpu
from src import comparation_methods as cmp
import cv2

video_path = '../../res/videos/'
video_format = '.mp4'
subject_quantity = 4

no_led_videos = vpu.get_no_led_videos()
led_videos = vpu.get_led_videos()

subject_videos = []

for n in no_led_videos:
    for l in led_videos:
        if n[2] == l[2]:
            subject_videos.append([n[0], n[2]])


no_led_blues = []
led_blues = []

for s in subject_videos:

    # without LED

    [r, g, b, f] = vpu.getFilteredRGBVectors(video_path + s[0] + '-sinled-' + s[1] + video_format,
                                             vpu.Location.CENTER, 30, 61)
    # R = np.abs(np.fft.fftshift(fft.fft_iter_opt(r))) ** 2
    # G = np.abs(np.fft.fftshift(fft.fft_iter_opt(g))) ** 2
    B = np.abs(np.fft.fftshift(fft.fft_iter_opt(b))) ** 2
    no_led_blues.append(abs(f[np.argmax(B)]) * 60)



    # with LED

    [r, g, b, f] = vpu.getFilteredRGBVectors(video_path + s[0] + '-led-' + s[1] + video_format, vpu.Location.CENTER, 30, 61)

    # R = np.abs(np.fft.fftshift(fft.fft_iter_opt(r))) ** 2
    # G = np.abs(np.fft.fftshift(fft.fft_iter_opt(g))) ** 2
    B = np.abs(np.fft.fftshift(fft.fft_iter_opt(b))) ** 2
    led_blues.append( abs(f[np.argmax(B)]) * 60)


cmp.bland_altman(np.asarray(no_led_blues), np.array(led_blues))
