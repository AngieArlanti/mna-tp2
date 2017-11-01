import numpy as np
from src.utils import video_processing_utils as vpu
import src.utils.tests_utils as tests_utils
from src.comparation_methods import get_coefficient_of_determination as r2
from src.utils.directory_utils import validateDirectories
from src.utils.plot_utils import plot_linear_regression

validateDirectories()

def test():

    led_resources = vpu.get_led_videos()
    no_led_resources = vpu.get_no_led_videos()

    resultR_led, resultG_led, resultB_led = show_obtained_vs_expected_results(":::RESULTADOS PARA MUESTRAS OBTENIDAS CON LED:::", led_resources)
    resultR_no_led, resultG_no_led, resultB_no_led = show_obtained_vs_expected_results(":::RESULTADOS PARA MUESTRAS OBTENIDAS SIN LED:::", no_led_resources)
    plot_linear_regression("Regresion lineal led", "led", "Esperados", "Obtenidos", np.array(resultG_led)[:, 0],
                           np.array(resultG_led)[:, 1])
    plot_linear_regression("Regresion lineal sin led", "no_led", "Esperados", "Obtenidos", np.array(resultG_no_led)[:, 0],
                           np.array(resultG_no_led)[:, 1])


def show_obtained_vs_expected_results(title, resources):

    print("Procesando...")
    print("")

    resultR, resultG, resultB = tests_utils.get_obtained_vs_expected(resources, vpu.Location.CENTER, 30, 60)
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

    return resultR, resultG, resultB

test()