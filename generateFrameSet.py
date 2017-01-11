#Function for extracting individual frame from directory of TIFF files

import matplotlib.pyplot as plt
import glob
import os
import numpy as np
np.set_printoptions(threshold=np.inf)
import scipy as sp
import sys

def FlattenTIFFData(TIFFdata, channel=1): #TIFFdata - NumPy array of raw TIFF data

    flat = TIFFdata[:,:, channel] #extract only single channel
    return flat; #return flattened data

def generateFrameFromTIFF(filePath): #filePath - path of individual image file to load

    image = plt.imread(filePath) #load TIFF file using matplotlib (with Pillow dependency)

    return image;

def generateFrameSet(filePath): #filePath - path of file directory containing TIFF files to load

    print ("TOP:    Loading script: generateFrameSet")
    print("LOG:    Start Frame Set Generation")
    frames = []
    fileList = glob.glob(filePath)
    print("LOG:       File list contains: " + str(len(fileList)) + " images")
    for file in fileList:
        print("LOG:    Load image name: " + file)
        frameInt = FlattenTIFFData(generateFrameFromTIFF(file))
        frameFloat = frameInt.astype(float)
        frames.append(frameFloat)
    print("LOG:    Returning frames")
    return frames;  #return list of frames




