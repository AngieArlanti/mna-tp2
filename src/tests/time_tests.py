
from src.utils import video_processing_utils as vpu
from src.utils import plot_utils as pu
from src.utils import fft_calc_utils as fcu





video_path = '../../res/videos/'
video_format = '.mp4'
videos = vpu.get_led_videos()
led_freqs = []

for v in videos:

    [r, g, b, f] = vpu.getFilteredRGBVectors(video_path + v[0] + '-' + v[1] + '-' + v[2] + video_format, vpu.Location.CENTER, 30, 61)
    [R,G,B] = fcu.runFFTWithMethod(fcu.FFTMethod.FFT_ITER_OPT,r,g,b,f)

    led_freqs.append([fcu.getHeartRateFromBandVector(R,f), fcu.getHeartRateFromBandVector(G,f), fcu.getHeartRateFromBandVector(B,f)])

fhr = vpu.getFitbitHeartRates(vpu.LedPreference.LED)
k=0
for x in led_freqs:
    for y in x:
        print(y)
        print(fhr[k])
        print(abs(y - fhr[k]))
    k+1

print(vpu.getFitbitHeartRates(vpu.LedPreference.LED))
print(led_freqs)
#print(vpu.getResourcesFromDirectory())

