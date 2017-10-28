
from src.utils import video_processing_utils as vpu
from src.utils import plot_utils as pu
from src.utils import fft_calc_utils as fcu


# videoName = 'fierens.mp4'
# videoName = 'arlanti.mp4'
#videoName = 'fierens.mp4'
videoName = '71.mp4'

video_path = '../../res/videos/'


[r, g, b, f] = vpu.getFilteredRGBVectors(video_path + videoName, vpu.Location.CENTER, 30,60)

[R,G,B] = fcu.runFFTWithMethod(fcu.FFTMethod.NUMPY_FFT,r,g,b,f)

pu.plotRGB(R,G,B,f)

