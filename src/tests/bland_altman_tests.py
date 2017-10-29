import numpy as np
from src.fft import fft
from src.utils import video_processing_utils as vpu
from src import comparation_methods as cmp

video_path = '../../res/videos/'
video_format = '.mp4'

no_led_videos = vpu.get_no_led_videos()
led_videos = vpu.get_led_videos()
fitbit_measures = vpu.get_fitbit_frequencies()

no_led_videos.sort(key=lambda x: int(x[0]))
led_videos.sort(key=lambda x: int(x[0]))
fitbit_measures.sort()

subject_quantity = len(fitbit_measures)

subject_videos = []

for l in led_videos:
    for n in no_led_videos:
        if n[2] == l[2]:
            subject_videos.append([l[0], l[2]])

no_led_reds = []
led_reds = []

no_led_greens = []
led_greens = []

no_led_blues = []
led_blues = []

for s in subject_videos:
    # without LED

    [r, g, b, f] = vpu.getFilteredRGBVectors(video_path + s[0] + '-sinled-' + s[1] + video_format,
                                             vpu.Location.CENTER, 30, 61)
    # R = np.abs(np.fft.fftshift(fft.fft_iter_opt(r))) ** 2
    # G = np.abs(np.fft.fftshift(fft.fft_iter_opt(g))) ** 2
    B = np.abs(np.fft.fftshift(fft.fft_iter_opt(b))) ** 2
    # no_led_reds.append(abs(f[np.argmax(R)]) * 60)
    # no_led_greens.append(abs(f[np.argmax(G)]) * 60)
    no_led_blues.append(abs(f[np.argmax(B)]) * 60)

    # with LED

    [r, g, b, f] = vpu.getFilteredRGBVectors(video_path + s[0] + '-led-' + s[1] + video_format, vpu.Location.CENTER, 30,
                                             61)

    # R = np.abs(np.fft.fftshift(fft.fft_iter_opt(r))) ** 2
    # G = np.abs(np.fft.fftshift(fft.fft_iter_opt(g))) ** 2
    B = np.abs(np.fft.fftshift(fft.fft_iter_opt(b))) ** 2
    # led_reds.append(abs(f[np.argmax(R)]) * 60)
    # led_greens.append(abs(f[np.argmax(G)]) * 60)
    led_blues.append(abs(f[np.argmax(B)]) * 60)

# cmp.bland_altman(fitbit_measures, np.asarray(led_reds),
#                  "Diagrama Bland-Altman para medidas con FitBit y canal rojo con LED")
# cmp.bland_altman(fitbit_measures, np.asarray(no_led_reds),
#                  "Diagrama Bland-Altman para medidas con FitBit y canal rojo sin LED")
# cmp.bland_altman(np.asarray(no_led_reds), np.asarray(led_reds),
#                  "Diagrama Bland-Altman para medidas del canal rojo con y sin LED")
#
# cmp.bland_altman(fitbit_measures, np.asarray(led_greens),
#                  "Diagrama Bland-Altman para medidas con FitBit y canal verde con LED")
# cmp.bland_altman(fitbit_measures, np.asarray(no_led_greens),
#                  "Diagrama Bland-Altman para medidas con FitBit y canal verde sin LED")
# cmp.bland_altman(np.asarray(no_led_greens), np.asarray(led_greens),
#                  "Diagrama Bland-Altman para medidas del canal verde con y sin LED")

cmp.bland_altman(fitbit_measures, np.asarray(led_blues),
                 "Diagrama Bland-Altman para medidas con FitBit y canal azul con LED")
cmp.bland_altman(fitbit_measures, np.asarray(no_led_blues),
                 "Diagrama Bland-Altman para medidas con FitBit y canal azul sin LED")
cmp.bland_altman(np.asarray(no_led_blues), np.asarray(led_blues),
                 "Diagrama Bland-Altman para medidas del canal azul con y sin LED")
