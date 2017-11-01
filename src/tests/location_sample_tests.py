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

locations = [vpu.Location.CENTER, vpu.Location.LEFT, vpu.Location.RIGHT, vpu.Location.LOWER_CENTER,
             vpu.Location.LOWER_LEFT, vpu.Location.LOWER_RIGHT, vpu.Location.UPPER_CENTER,
             vpu.Location.UPPER_LEFT, vpu.Location.UPPER_RIGHT]
obtained_vs_expected_G_CENTER = []
obtained_vs_expected_G_LEFT = []
obtained_vs_expected_G_RIGHT = []
obtained_vs_expected_G_LOWER_CENTER = []
obtained_vs_expected_G_LOWER_LEFT = []
obtained_vs_expected_G_LOWER_RIGHT = []
obtained_vs_expected_G_UPPER_CENTER = []
obtained_vs_expected_G_UPPER_LEFT = []
obtained_vs_expected_G_UPPER_RIGHT = []

for res in resources:
    print(res[3])
    for location in locations:
        [r, g, b, f] = vpu.getFilteredRGBVectors(video_path + res[3], location, 30, 60)
        [R, G, B] = fcu.runFFTWithMethod(fcu.FFTMethod.FFT_ITER_OPT, r, g, b, f)
        gFrec = abs(f[np.argmax(G)]) * 60
        auxG = []
        auxG.append(res[3])
        auxG.append(location.name)
        auxG.append(float(gFrec))
        auxG.append(float(res[0]))
        if location == vpu.Location.CENTER:
            obtained_vs_expected_G_CENTER.append(auxG)
        elif location == vpu.Location.LEFT:
            obtained_vs_expected_G_LEFT.append(auxG)
        elif location == vpu.Location.RIGHT:
            obtained_vs_expected_G_RIGHT.append(auxG)
        elif location == vpu.Location.LOWER_CENTER:
            obtained_vs_expected_G_LOWER_CENTER.append(auxG)
        elif location == vpu.Location.LOWER_LEFT:
            obtained_vs_expected_G_LOWER_LEFT.append(auxG)
        elif location == vpu.Location.LOWER_RIGHT:
            obtained_vs_expected_G_LOWER_RIGHT.append(auxG)
        elif location == vpu.Location.UPPER_CENTER:
            obtained_vs_expected_G_UPPER_CENTER.append(auxG)
        elif location == vpu.Location.UPPER_LEFT:
            obtained_vs_expected_G_UPPER_LEFT.append(auxG)
        else:
            obtained_vs_expected_G_UPPER_RIGHT.append(auxG)


# obtained_vs_expected_G_CENTER = np.array(obtained_vs_expected_G_CENTER).astype(np.float)
# obtained_vs_expected_G_LEFT = np.array(obtained_vs_expected_G_LEFT).astype(np.float)
# obtained_vs_expected_G_RIGHT = np.array(obtained_vs_expected_G_RIGHT).astype(np.float)
# obtained_vs_expected_G_LOWER_CENTER = np.array(obtained_vs_expected_G_LOWER_CENTER).astype(np.float)
# obtained_vs_expected_G_LOWER_LEFT = np.array(obtained_vs_expected_G_LOWER_LEFT).astype(np.float)
# obtained_vs_expected_G_LOWER_RIGHT = np.array(obtained_vs_expected_G_LOWER_RIGHT).astype(np.float)

print("     File     ", " | ", "     Location     ", " | ""     Obtained     ", " | ", "     Expected     ")
show_results(obtained_vs_expected_G_CENTER)
show_results(obtained_vs_expected_G_LEFT)
show_results(obtained_vs_expected_G_RIGHT)
show_results(obtained_vs_expected_G_LOWER_CENTER)
show_results(obtained_vs_expected_G_LOWER_LEFT)
show_results(obtained_vs_expected_G_LOWER_RIGHT)
show_results(obtained_vs_expected_G_UPPER_CENTER)
show_results(obtained_vs_expected_G_UPPER_LEFT)
show_results(obtained_vs_expected_G_UPPER_RIGHT)

pearsonGCENTER = r2((np.array(obtained_vs_expected_G_CENTER)[:,2]).astype(np.float),
                    (np.array(obtained_vs_expected_G_CENTER)[:,3]).astype(np.float))
pearsonGLEFT = r2((np.array(obtained_vs_expected_G_LEFT)[:,2]).astype(np.float),
                  (np.array(obtained_vs_expected_G_LEFT)[:,3]).astype(np.float))
pearsonGRIGHT = r2((np.array(obtained_vs_expected_G_RIGHT)[:,2]).astype(np.float),
                   (np.array(obtained_vs_expected_G_RIGHT)[:,3]).astype(np.float))
pearsonGLOWER_CENTER = r2((np.array(obtained_vs_expected_G_LOWER_CENTER)[:,2]).astype(np.float),
                          (np.array(obtained_vs_expected_G_LOWER_CENTER)[:,3]).astype(np.float))
pearsonGLOWER_LEFT = r2((np.array(obtained_vs_expected_G_LOWER_LEFT)[:,2]).astype(np.float),
                        (np.array(obtained_vs_expected_G_LOWER_LEFT)[:,3]).astype(np.float))
pearsonGLOWER_RIGHT = r2((np.array(obtained_vs_expected_G_LOWER_RIGHT)[:,2]).astype(np.float),
                         (np.array(obtained_vs_expected_G_LOWER_RIGHT)[:,3]).astype(np.float))
pearsonGUPPER_CENTER = r2((np.array(obtained_vs_expected_G_UPPER_CENTER)[:,2]).astype(np.float),
                         (np.array(obtained_vs_expected_G_UPPER_CENTER)[:,3]).astype(np.float))
pearsonGUPPER_LEFT = r2((np.array(obtained_vs_expected_G_UPPER_LEFT)[:,2]).astype(np.float),
                         (np.array(obtained_vs_expected_G_UPPER_LEFT)[:,3]).astype(np.float))
pearsonGUPPER_RIGHT = r2((np.array(obtained_vs_expected_G_UPPER_RIGHT)[:,2]).astype(np.float),
                         (np.array(obtained_vs_expected_G_UPPER_RIGHT)[:,3]).astype(np.float))

print("Coeficiente de determinación R2 de Pearson para G  CENTER: ", pearsonGCENTER)
print("Coeficiente de determinación R2 de Pearson para G  LEFT: ", pearsonGLEFT)
print("Coeficiente de determinación R2 de Pearson para G  RIGHT: ", pearsonGRIGHT)
print("Coeficiente de determinación R2 de Pearson para G  LOWER_CENTER: ", pearsonGLOWER_CENTER)
print("Coeficiente de determinación R2 de Pearson para G  LOWER_LEFT: ", pearsonGLOWER_LEFT)
print("Coeficiente de determinación R2 de Pearson para G  LOWER_RIGHT: ", pearsonGLOWER_RIGHT)
print("Coeficiente de determinación R2 de Pearson para G  UPPER_CENTER: ", pearsonGUPPER_CENTER)
print("Coeficiente de determinación R2 de Pearson para G  UPPER_LEFT: ", pearsonGUPPER_LEFT)
print("Coeficiente de determinación R2 de Pearson para G  UPPER_RIGHT: ", pearsonGUPPER_RIGHT)

