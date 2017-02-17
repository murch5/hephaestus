import matplotlib.pyplot as plt
import numpy as np
import sys
import scipy as sp
import image as image
import generateFrameSet


class contourMap(image.image):

    def initContourMap(self):

        dim = self.surfaceData.shape

        self.x = np.arange(0, dim[0])
        self.y = np.arange(0, dim[1])
        self.addLinesFlag = False
        self.lineDrawFunc = None
        self.meshX, self.meshY = np.meshgrid(self.x, self.y)

        return

    def __init__(self, figure, data, position,title="",plotArgs=[]):
        image.image.__init__(self, figure, data, position,title,plotArgs)
        self.surfaceData = data[0]
        self.currFrame = data[0]
        self.x = []
        self.y = []
        self.meshX = []
        self.meshY = []
        self.contourPlot = []

        self.subplot.axis("equal")

        self.initContourMap()

        return

    def draw(self):
       # print("LOG:    Draw initial step of contour map")
        self.subplot.cla()
        levels =[11,17,20,40,80]
        self.contourPlot = self.subplot.contour(self.meshX, self.meshY, self.surfaceData.T, zdir='z',linewidths=1,cmap="viridis", levels=levels)
        self.image = self.contourPlot
        if self.addLinesFlag == True:
            self.lineDrawFunc()

        if self.retrieveArgVal("colorBar") is not None:
            self.clearColorBar()
            self.addColorBar(self.contourPlot)

        self.colorBar.outline.set_linewidth(0.2)
        for line in self.colorBar.lines:
            line.set_linewidth(5.0)

        if len(self.xlim) > 0:
            self.subplot.set_xlim(self.xlim)
        if len(self.ylim) > 0:
            self.subplot.set_ylim(self.ylim)

        self.subplot.invert_yaxis()

        return

    def setSurfaceData(self, data):
        self.surfaceData = data.T
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

        self.draw()

        return self.subplot

    def initAnimate(self, i):
        self.draw()
        return;