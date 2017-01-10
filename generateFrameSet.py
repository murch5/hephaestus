#Function for extracting individual frame from directory of TIFF files

import glob
import os

def generateFrameSet(filePath): #filePath - path of file directory containing TIFF files to load

    for name in glob.glob(filePath):
        print(name)

    return;

generateFrameSet("*")