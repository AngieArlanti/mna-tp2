from scipy.stats import pearsonr as r2

import numpy as np

def get_coefficient_of_determination(x,y):

    #y = np.array([1.2,1.3,1.6,1.9])
    #x = np.array([1.4,2.3,1.5,1.6])
    coefficient_of_dermination = r2(y, x)
    print("Coeficiente de pearson: ", coefficient_of_dermination[0])


