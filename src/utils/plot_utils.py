import matplotlib.pyplot as plt
import numpy as np

from src.utils.directory_utils import validateDirectories

validateDirectories()

def plotRGB(R, G, B, f):
    plt.xlabel("frecuencia cardiaca [1/minuto]")
    plt.plot(60 * f, R, "r")
    plt.xlim(0, 200)

    plt.plot(60 * f, G, "g")
    plt.xlim(0, 200)

    plt.plot(60 * f, B, "b")
    plt.xlim(0, 200)

    plt.show()

def plot_linear_regression(title,file, xlabel, ylabel, x, y):
    fit = np.polyfit(x, y, 1)
    fit_fn = np.poly1d(fit)
    # fit_fn is now a function which takes in x and returns an estimate for y
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.plot(x, y, 'yo', x, fit_fn(x), '--k')
    plt.savefig("../../out/linear_regression_" +  file + ".png")
    plt.close()