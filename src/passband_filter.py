from scipy.signal import butter, lfilter


class PBFilter:

    low = 50
    high = 130

    order = 2

    btype = 'band'

    def __init__(self):
        pass

    @staticmethod
    def filter(channel, fps):
        butter_range = [(PBFilter.low / 60) / fps * 2, (PBFilter.high / 60) / fps * 2]

        b, a = butter(PBFilter.order, butter_range, PBFilter.btype)

        return lfilter(b, a, channel)
