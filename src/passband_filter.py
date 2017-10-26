import numpy as np

from scipy.signal import butter, lfilter


class PBFilter:

    low = 50
    high = 130
    order = 2
    btype = 'band'

    def __init__(self):
        pass

    def filter(self, channel, fps):
        return self.butter_bandpass_filter(channel, fps)

    def butter_bandpass_filter(self, data, fps):
        b, a = butter(self.order, self.bpm_range(fps), self.btype)
        y = lfilter(b, a, data)
        return y

    def bpm_range(self, fps):
        return [
            (self.low / 60) / fps * 2,
            (self.high / 60) / fps * 2,
        ]
