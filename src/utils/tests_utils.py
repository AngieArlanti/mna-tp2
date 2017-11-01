from src.utils import video_processing_utils as vpu
import numpy as np
from src.utils import fft_calc_utils as fcu

RES_DIRECTORY = '../../res/videos/'

def get_obtained_vs_expected(resources):

    obtained_vs_expected_R = []
    obtained_vs_expected_G = []
    obtained_vs_expected_B = []

    for res in resources:
        print(res[3])
        [r, g, b, f] = vpu.getFilteredRGBVectors(RES_DIRECTORY + res[3], vpu.Location.CENTER, 30, 60)
        [R, G, B] = fcu.runFFTWithMethod(fcu.FFTMethod.FFT_ITER_OPT, r, g, b, f)
        rFrec = abs(f[np.argmax(R)]) * 60
        gFrec = abs(f[np.argmax(G)]) * 60
        bFrec = abs(f[np.argmax(B)]) * 60

        auxR = []
        auxR.append(rFrec)
        auxR.append(res[0])
        obtained_vs_expected_R.append(auxR)

        auxG = []
        auxG.append(gFrec)
        auxG.append(res[0])
        obtained_vs_expected_G.append(auxG)

        auxB = []
        auxB.append(bFrec)
        auxB.append(res[0])
        obtained_vs_expected_B.append(auxB)

    obtained_vs_expected_R = np.array(obtained_vs_expected_R).astype(np.float)
    obtained_vs_expected_G = np.array(obtained_vs_expected_G).astype(np.float)
    obtained_vs_expected_B = np.array(obtained_vs_expected_B).astype(np.float)

    return obtained_vs_expected_R, obtained_vs_expected_G, obtained_vs_expected_B
