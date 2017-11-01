import numpy as np
from src.utils import video_processing_utils as vpu

from src.utils import fft_calc_utils as fcu
from src.comparation_methods import get_coefficient_of_determination as r2
from src.utils.directory_utils import validateDirectories

validateDirectories()

def show_results(result):
    for data in result:
        print("  ", data[0], "   | ", "       ", data[1], "   | ", "       ", data[2], "   | ", "       ", data[3])

    print("")


video_path = '../../res/videos/'

resources = vpu.get_led_videos()

sizes = [10, 20, 30, 40, 50, 60]

obtained_vs_expected_G_size_10 = []
obtained_vs_expected_G_size_20 = []
obtained_vs_expected_G_size_30 = []
obtained_vs_expected_G_size_40 = []
obtained_vs_expected_G_size_50 = []
obtained_vs_expected_G_size_60 = []


for res in resources:
    print(res[3])
    for size in sizes:
        [r, g, b, f] = vpu.getFilteredRGBVectors(video_path + res[3], vpu.Location.UPPER_LEFT, size, 60)
        [R, G, B] = fcu.runFFTWithMethod(fcu.FFTMethod.FFT_ITER_OPT, r, g, b, f)
        gFrec = abs(f[np.argmax(G)]) * 60
        auxG = []
        auxG.append(res[3])
        auxG.append(size)
        auxG.append(float(gFrec))
        auxG.append(float(res[0]))
        if size == 10:
            obtained_vs_expected_G_size_10.append(auxG)
        elif size == 20:
            obtained_vs_expected_G_size_20.append(auxG)
        elif size == 30:
            obtained_vs_expected_G_size_30.append(auxG)
        elif size == 40:
            obtained_vs_expected_G_size_40.append(auxG)
        elif size == 50:
            obtained_vs_expected_G_size_50.append(auxG)
        else:
            obtained_vs_expected_G_size_60.append(auxG)


# obtained_vs_expected_G_CENTER = np.array(obtained_vs_expected_G_CENTER).astype(np.float)
# obtained_vs_expected_G_LEFT = np.array(obtained_vs_expected_G_LEFT).astype(np.float)
# obtained_vs_expected_G_RIGHT = np.array(obtained_vs_expected_G_RIGHT).astype(np.float)
# obtained_vs_expected_G_LOWER_CENTER = np.array(obtained_vs_expected_G_LOWER_CENTER).astype(np.float)
# obtained_vs_expected_G_LOWER_LEFT = np.array(obtained_vs_expected_G_LOWER_LEFT).astype(np.float)
# obtained_vs_expected_G_LOWER_RIGHT = np.array(obtained_vs_expected_G_LOWER_RIGHT).astype(np.float)

print("     File     ", " | ", "     Location     ", " | ""     Obtained     ", " | ", "     Expected     ")
show_results(obtained_vs_expected_G_size_10)
show_results(obtained_vs_expected_G_size_20)
show_results(obtained_vs_expected_G_size_30)
show_results(obtained_vs_expected_G_size_40)
show_results(obtained_vs_expected_G_size_50)
show_results(obtained_vs_expected_G_size_60)


pearsonG10 = r2((np.array(obtained_vs_expected_G_size_10)[:,2]).astype(np.float),
                    (np.array(obtained_vs_expected_G_size_10)[:,3]).astype(np.float))
pearsonG20 = r2((np.array(obtained_vs_expected_G_size_20)[:,2]).astype(np.float),
                  (np.array(obtained_vs_expected_G_size_20)[:,3]).astype(np.float))
pearsonG30 = r2((np.array(obtained_vs_expected_G_size_30)[:,2]).astype(np.float),
                   (np.array(obtained_vs_expected_G_size_30)[:,3]).astype(np.float))
pearsonG40 = r2((np.array(obtained_vs_expected_G_size_40)[:,2]).astype(np.float),
                          (np.array(obtained_vs_expected_G_size_40)[:,3]).astype(np.float))
pearsonG50 = r2((np.array(obtained_vs_expected_G_size_50)[:,2]).astype(np.float),
                        (np.array(obtained_vs_expected_G_size_50)[:,3]).astype(np.float))
pearsonG60 = r2((np.array(obtained_vs_expected_G_size_60)[:,2]).astype(np.float),
                         (np.array(obtained_vs_expected_G_size_60)[:,3]).astype(np.float))

print("Coeficiente de determinación R2 de Pearson para G  10: ", pearsonG10)
print("Coeficiente de determinación R2 de Pearson para G  20: ", pearsonG20)
print("Coeficiente de determinación R2 de Pearson para G  30: ", pearsonG30)
print("Coeficiente de determinación R2 de Pearson para G  40: ", pearsonG40)
print("Coeficiente de determinación R2 de Pearson para G  50: ", pearsonG50)
print("Coeficiente de determinación R2 de Pearson para G  60: ", pearsonG60)

