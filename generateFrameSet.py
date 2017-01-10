#Function for extracting individual frame from directory of TIFF files

import matplotlib.pyplot as plt
import glob
import os
import numpy as np
import scipy as sp

def generateFrameSet(filePath): #filePath - path of file directory containing TIFF files to load

    print("LOG:    Start Frame Set Generation")
    frames = []
    fileList = glob.glob(filePath)
    for file in fileList:
        print("LOG:    Image Name: " + file)
        frame.append(generateFrameFromTIFF(file))

    return;

generateFrameSet("*.tiff")


def FlattenTIFFData(TIFFdata): #TIFFdata - NumPy array of raw TIFF data


    return;

def generateFrameFromTIFF(filePath): #filePath - path of individual image file to load

    image = plt.imread(filePath)

    return;
