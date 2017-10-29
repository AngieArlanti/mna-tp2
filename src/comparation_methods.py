from scipy.stats import pearsonr as r2
import matplotlib.pyplot as plt
import numpy as np
import hashlib


def get_coefficient_of_determination(x, y):
    # Pearson coefficient varies between -1 and +1
    # with 0 implying no correlation. Correlations of -1 or +1 imply an exact
    # linear relationship. Positive correlations imply that as x increases, so
    # does y. Negative correlations imply that as x increases, y decreases.
    coefficient_of_dermination = r2(y, x)
    return coefficient_of_dermination[0]


def bland_altman(x, y, title):
    mean = np.mean([x, y], axis=0)
    diff = x - y  # Difference between x and y
    md = np.mean(diff)  # Mean of the difference
    sd = np.std(diff, axis=0)  # Standard deviation of the difference

    plt.title(title)
    plt.scatter(mean, diff)

    plt.axhline(md, color='gray', linestyle='--')
    plt.axhline(md + 1.96 * sd, color='gray', linestyle='--')
    plt.axhline(md - 1.96 * sd, color='gray', linestyle='--')

    plt.xlabel("promedio de mediciones [1/minuto]")
    plt.ylabel("diferencia entre mediciones [1/minuto]")

    hash_object = hashlib.md5(diff)
    plt.savefig("../../out/B&A_" + hash_object.hexdigest() + ".png")

    plt.show()
