import numpy as np
from src.utils import video_processing_utils as vpu

from src.utils import fft_calc_utils as fcu
from src.comparation_methods import get_coefficient_of_determination as r2

RES_DIRECTORY = '../../res/videos/'

fileNames = vpu.getValidFileNames()
resources = vpu.getResourcesFromDirectory()

obtainedR = []
obtainedG = []
obtainedB = []
expected = []
i=0;
for name in fileNames:
    [r, g, b, f] = vpu.getFilteredRGBVectors(RES_DIRECTORY+name, vpu.Location.CENTER, 30, 60)
    [R, G, B] = fcu.runFFTWithMethod(fcu.FFTMethod.FFT_ITER_OPT, r, g, b, f)
    rFrec = abs(f[np.argmax(R)]) * 60
    gFrec = abs(f[np.argmax(G)]) * 60
    bFrec = abs(f[np.argmax(B)]) * 60
    obtainedR.append(rFrec)
    obtainedG.append(gFrec)
    obtainedB.append(bFrec)
    expected.append(resources[i][0])
    i=i+1

expected = np.array(expected).astype(np.float)
print("obtained R: ", obtainedR)
print("obtained G: ", obtainedG)
print("obtained B: ", obtainedB)
print("expected: ", expected)
print(resources)

pearsonR = r2(expected,obtainedR)
pearsonG = r2(expected,obtainedG)
pearsonB = r2(expected,obtainedB)

print("Coeficiente de determinación R2 de Pearson para R: ",pearsonR)
print("Coeficiente de determinación R2 de Pearson para G: ",pearsonG)
print("Coeficiente de determinación R2 de Pearson para B: ",pearsonB)


