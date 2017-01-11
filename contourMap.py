import matplotlib.pyplot as plt
import numpy as np
import sys
import scipy as sp

import generateFrameSet

class contourMap:

    def initContourMap(self):
        dim = self.surfaceData.shape
        print(dim)

        self.x = np.arange(0, dim[0])
        self.y = np.arange(0, dim[1])

        self.X,self.Y = np.meshgrid(self.x,self.y)

        return;

    def __init__(self,data,targetSubplot):
        self.surfaceData = data
        self.x = []
        self.y = []
        self.meshX = []
        self.meshY = []
        self.subplot = targetSubplot

        self.initContourMap()

        return;

    def drawContour(self):
        return;

