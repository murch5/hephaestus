import matplotlib.pyplot as plt
import numpy as np
import sys
import scipy as sp
import animPlot as animPlot
import generateFrameSet


class contourMap(animPlot.animPlot):

    def initContourMap(self):

        dim = self.surfaceData.shape

        self.x = np.arange(0, dim[0])
        self.y = np.arange(0, dim[1])
        self.addLinesFlag = False
        self.lineDrawFunc = None
        self.meshX, self.meshY = np.meshgrid(self.x, self.y)

        return

    def __init__(self, figure, data, position):
        animPlot.animPlot.__init__(self, figure, data, position)
        self.surfaceData = data[0]
        self.x = []
        self.y = []
        self.meshX = []
        self.meshY = []
        self.contourPlot = []



        self.initContourMap()

        return

    def draw(self):
       # print("LOG:    Draw initial step of contour map")
        self.contourPlot = self.subplot.contour(self.meshX, self.meshY, self.surfaceData.T, zdir='z',linewidths=1,cmap="viridis")
        if self.addLinesFlag == True:
            self.lineDrawFunc()
        return

    def setSurfaceData(self, data):
        self.surfaceData = data
        return

    def assignLineDrawFunc(self,lineFunc):

        self.addLinesFlag = True
        self.lineDrawFunc = lineFunc

        return;

    def animate(self,i):
        self.currFrameIndex += 1

        if self.currFrameIndex == self.framesPerImage:
            self.currFrameIndex = 0
            self.currImageIndex += 1

        if self.currImageIndex == len(self.frames) - 1:
            self.currFrameIndex = 0
            self.currImageIndex = 0

        it = np.nditer(self.currFrame, flags=['multi_index'])
        while not it.finished:
            self.currFrame[it.multi_index] = self.frames[self.currImageIndex][it.multi_index] + ((self.frames[(
            self.currImageIndex + 1)][it.multi_index] - self.frames[self.currImageIndex][it.multi_index]) * (
                                                                                                 self.currFrameIndex / 20))

            it.iternext()

        self.surfaceData = self.currFrame
        self.subplot.clear()
        contourMap.draw(self)
        return self.subplot

    def initAnimate(self, i):
        self.draw()
        return;