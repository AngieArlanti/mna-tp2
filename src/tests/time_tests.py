
from src.utils import video_processing_utils as vpu
from src.utils import plot_utils as pu
from src.utils import fft_calc_utils as fcu
from src.utils.directory_utils import validateDirectories
from src.comparation_methods import get_coefficient_of_determination as r2

video_path = '../../res/videos/'
video_format = '.mp4'

validateDirectories()


videos = vpu.get_led_videos()
led_freqs = []

times = [1,5,10,20,30,45,60]
redHeartrates = []
greenHeartrates = []
blueHeartrates = []
rgbHeartrates = []
displayMatrix = []

print("[Red channel R2 coefficient]"+'\t'+"[Green channel R2 coefficient]"+'\t'+"[Blue channel R2 coefficient]"+'\t'+"[Video length in seconds]")
for t in times:
    k = 0
    for v in videos:

        [r, g, b, f] = vpu.getFilteredRGBVectors(video_path + v[0] + '-' + v[1] + '-' + v[2] + video_format, vpu.Location.CENTER, 40, t)
        [R,G,B] = fcu.runFFTWithMethod(fcu.FFTMethod.FFT_ITER_OPT,r,g,b,f)
        redHeartrates.append(fcu.getHeartRateFromBandVector(R,f))
        greenHeartrates.append(fcu.getHeartRateFromBandVector(G, f))
        blueHeartrates.append(fcu.getHeartRateFromBandVector(B, f))
        led_freqs.append([fcu.getHeartRateFromBandVector(R,f), fcu.getHeartRateFromBandVector(G,f), fcu.getHeartRateFromBandVector(B,f)])

    fitbit = vpu.getFitbitHeartRates(vpu.LedPreference.LED)
    rgbHeartrates.append([redHeartrates,greenHeartrates,blueHeartrates,fitbit])
    pearsonR = r2(redHeartrates,fitbit)
    pearsonG = r2(greenHeartrates,fitbit)
    pearsonB = r2(blueHeartrates,fitbit)
    print([str(pearsonR),str(pearsonG),str(pearsonB),str(t)])

    redHeartrates = []
    greenHeartrates = []
    blueHeartrates = []
    k = k+1

fhr = vpu.getFitbitHeartRates(vpu.LedPreference.LED)
k=0
for x in led_freqs:
        x.append(fhr[k%len(fhr)])
k=k+1



print("----------------------------------------------------------------------------------")
print("Red"+'\t'+"Green"+'\t'+"Blue"+'\t'+"Fitbit measure")
s = [[str(e) for e in row] for row in led_freqs]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]
print('\n'.join(table))

