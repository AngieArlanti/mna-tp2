
from src.utils import video_processing_utils as vpu
from src.utils import plot_utils as pu
from src.utils import fft_calc_utils as fcu
import numpy as np
from src.comparation_methods import r2




video_path = '../../res/videos/'
video_format = '.mp4'
videos = vpu.get_led_videos()
led_freqs = []

times = [10,15,20,25,30,60]

for t in times:
    for v in videos:

        [r, g, b, f] = vpu.getFilteredRGBVectors(video_path + v[0] + '-' + v[1] + '-' + v[2] + video_format, vpu.Location.CENTER, 30, t)
        [R,G,B] = fcu.runFFTWithMethod(fcu.FFTMethod.FFT_ITER_OPT,r,g,b,f)

        led_freqs.append([fcu.getHeartRateFromBandVector(R,f), fcu.getHeartRateFromBandVector(G,f), fcu.getHeartRateFromBandVector(B,f)])


fhr = vpu.getFitbitHeartRates(vpu.LedPreference.LED)
k=0
for x in led_freqs:
    x.append(fhr[k%len(fhr)])
    k=k+1

#print(vpu.getFitbitHeartRates(vpu.LedPreference.LED))
#print(led_freqs)

s = [[str(e) for e in row] for row in led_freqs]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]
print('\n'.join(table))
#print(vpu.getResourcesFromDirectory())


