from scipy.signal import butter, lfilter


class PBFilter:

    low = 50
    high = 130
    order = 2
    btype = 'band'

    def __init__(self):
        pass

    def filter(self, channel, fps):
        return self._butter_bandpass_filter(channel, fps)

    def _butter_bandpass_filter(self, data, fps):
        b, a = butter(self.order, self._bpm_range(fps), self.btype)
        y = lfilter(b, a, data)
        return y

    def _bpm_range(self, fps):
        return [
            (self.low / 60) / fps * 2,
            (self.high / 60) / fps * 2,
        ]
