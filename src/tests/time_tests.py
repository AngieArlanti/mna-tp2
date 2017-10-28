
from src.utils import video_processing_utils as vpu
from src.utils import plot_utils as pu
from src.utils import fft_calc_utils as fcu

video_path = '../../res/videos/'
filenames = vpu.getValidFileNames()

for filename in filenames:
    [r, g, b, f] = vpu.getFilteredRGBVectors(video_path+filename, vpu.Location.CENTER, 30,60)
    [R,G,B] = fcu.runFFTWithMethod(fcu.FFTMethod.NUMPY_FFT,r,g,b,f)


pu.plotRGB(R,G,B,f)