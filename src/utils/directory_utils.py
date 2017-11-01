import os

def validateDirectories():
    videoPath = "../../res/videos"
    outPath = "../../out"
    if not os.path.exists(videoPath):
        os.makedirs(videoPath)
    if not os.path.exists(outPath):
        os.makedirs(outPath)