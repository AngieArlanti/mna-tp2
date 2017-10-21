from scipy.stats import pearsonr as r2

def get_coefficient_of_determination(x,y):

    #Pearson coefficient varies between -1 and +1
    #with 0 implying no correlation. Correlations of -1 or +1 imply an exact
    #linear relationship. Positive correlations imply that as x increases, so
    #does y. Negative correlations imply that as x increases, y decreases.
    coefficient_of_dermination = r2(y, x)
    print("Coeficiente de pearson: ", coefficient_of_dermination[0])


