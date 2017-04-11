import contourMapAnim as cm

import numpy as np
from matplotlib import lines as ln
import matplotlib.collections as collect
from contourMapAnim import contourMapAnim


class zbPeristalsis(contourMapAnim):

    def drawLines(self):

        self.lineCollection = collect.LineCollection(self.lineCoordFormatted,linewidths=1,colors=(0,0,0))
        self.subplot.add_collection(self.lineCollection)
          #  self.contourAnimationHandler.subplot.add_line(ln.Line2D(boundaryLines[:,0],boundaryLines[:,1]))
        return;

    def initLines(self):


        for lineSet in self.lineCoord:
            x = lineSet[:, 0]
            y = lineSet[:, 1]
            self.lineCoordFormatted.append(list(zip(x,y)))

        return;
    def loadBoundaryCoord(self,fileNames):

        for file in fileNames:
            d = np.loadtxt(file)
            self.lineCoord.append(d)
        return;

    def drawBoundaryCoord(self):
        self.assignLineDrawFunc(self.drawLines)

        return;

    def __init__(self, figure, data, position,title="",plotArgs=[],annotate=[]):
        contourMapAnim.__init__(self,figure,data,position,title,plotArgs,annotate=[])
        #self.contourAnimationHandler = cm.contourMapAnim(gf.generateFrameSet("*.tif"))
        self.lineCoord = []
        self.lineCoordFormatted = []
        self.lineCollection = None
        self.position = position
        fileNames = []

        fileNames.append(self.retrieveArgVal("boundary") + "Bottom.txt")
        fileNames.append(self.retrieveArgVal("boundary") + "Top.txt")
        self.loadBoundaryCoord(fileNames)
        self.drawBoundaryCoord()
        self.initLines()

        self.subplot.axis("equal")





