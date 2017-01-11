import matplotlib.pyplot as plt
import numpy as np
import sys
import scipy as sp

import generateFrameSet

class contourMap:

    def initContourMap(self):
        dim = self.surfaceData.shape

        self.x = np.arange(0, dim[0])
        self.y = np.arange(0, dim[1])

        self.meshX,self.meshY = np.meshgrid(self.x,self.y)

        return;

    def __init__(self,data,targetSubplot):
        self.surfaceData = data
        self.x = []
        self.y = []
        self.meshX = []
        self.meshY = []
        self.contourPlot = []

        self.subplot = targetSubplot

        self.initContourMap()

        return;

    def drawContour(self):
        print("LOG:    Draw initial step of contour map")
        self.contourPlot = self.subplot.contour(self.meshX,self.meshY,self.surfaceData,zdir='z', offset=-20, cmap="coolwarm")
        return;

    def setSurfaceData(self,data):
        self.surfaceData = data
        return;
