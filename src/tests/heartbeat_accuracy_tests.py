import numpy as np
from src.utils import video_processing_utils as vpu

from src.utils import fft_calc_utils as fcu
from src.comparation_methods import get_coefficient_of_determination as r2

RES_DIRECTORY = '../../res/videos/'

def test():

    led_resources = vpu.get_led_videos()
    no_led_resources = vpu.get_no_led_videos()

    show_obtained_vs_expected_results(":::RESULTADOS PARA MUESTRAS OBTENIDAS CON LED:::", led_resources)
    show_obtained_vs_expected_results(":::RESULTADOS PARA MUESTRAS OBTENIDAS SIN LED:::", no_led_resources)


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

def show_obtained_vs_expected_results(title, resources):

    print("Procesando...")
    print("")

    resultR, resultG, resultB = get_obtained_vs_expected(resources)
    print("")
    print("")
    print("::::::::::::::::::::::::::::::::::::::::::::::::")
    print(title)
    print("::::::::::::::::::::::::::::::::::::::::::::::::")
    print("")
    print("")
    print("     Obtained     ", " | ", "     Expected     ")
    for data in resultG:
        print("  ", data[0],"   | " ,"       ",data[1])

    print("")
    # np.array(resultR)[:, 0] = obtained column
    # np.array(resultR)[:, 1] = expected column
    pearsonR = r2(np.array(resultR)[:, 0], np.array(resultR)[:, 1])
    pearsonG = r2(np.array(resultG)[:, 0], np.array(resultG)[:, 1])
    pearsonB = r2(np.array(resultB)[:, 0], np.array(resultB)[:, 1])

    print("Coeficiente de determinación R2 de Pearson para R: ", pearsonR)
    print("Coeficiente de determinación R2 de Pearson para G: ", pearsonG)
    print("Coeficiente de determinación R2 de Pearson para B: ", pearsonB)
    print("")
    print("")
    print("::::::::::::::::::::::::::::::::::::::::::::::::")
    print("::::::::::::::::::::::::::::::::::::::::::::::::")
    print("::::::::::::::::::::::::::::::::::::::::::::::::")
    print("")
    print("")


test()