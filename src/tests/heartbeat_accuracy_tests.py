import numpy as np
from src.utils import video_processing_utils as vpu
import src.utils.tests_utils as tests_utils
from src.comparation_methods import get_coefficient_of_determination as r2
from src.utils.directory_utils import validateDirectories

validateDirectories()

def test():

    led_resources = vpu.get_led_videos()
    no_led_resources = vpu.get_no_led_videos()

    show_obtained_vs_expected_results(":::RESULTADOS PARA MUESTRAS OBTENIDAS CON LED:::", led_resources)
    show_obtained_vs_expected_results(":::RESULTADOS PARA MUESTRAS OBTENIDAS SIN LED:::", no_led_resources)

def show_obtained_vs_expected_results(title, resources):

    print("Procesando...")
    print("")

    resultR, resultG, resultB = tests_utils.get_obtained_vs_expected(resources)
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