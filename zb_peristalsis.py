import contourMapAnim as cm
import generateFrameSet as gf
import numpy as np
from matplotlib import lines as ln
import matplotlib.collections as collect
from contourMapAnim import contourMapAnim
from plot_manager import plot_manager

class zbPeristalsis(contourMapAnim):

    def drawLines(self):

        self.lineCollection = collect.LineCollection(self.lineCoordFormatted,linewidths=1)
        self.subplot.add_collection(self.lineCollection)
        print(self.lineCollection.get_array())
          #  self.contourAnimationHandler.subplot.add_line(ln.Line2D(boundaryLines[:,0],boundaryLines[:,1]))
        return;

    def initLines(self):
        print(self.lineCoord)

        for lineSet in self.lineCoord:
            x = lineSet[:, 0]
            y = lineSet[:, 1]
            self.lineCoordFormatted.append(list(zip(y,x)))
        print(self.lineCoordFormatted)
        return;
    def loadBoundaryCoord(self,fileNames):

        for file in fileNames:
            d = np.loadtxt(file)
            self.lineCoord.append(d)
        return;

    def drawBoundaryCoord(self):
        self.assignLineDrawFunc(self.drawLines)

        return;

    def __init__(self,figure, data, position):
        contourMapAnim.__init__(self,figure,data,position)
        #self.contourAnimationHandler = cm.contourMapAnim(gf.generateFrameSet("*.tif"))
        self.lineCoord = []
        self.lineCoordFormatted = []
        self.lineCollection = None
        self.position = position
        fileNames = []

        fileNames.append("Bottom.txt")
        fileNames.append("Top.txt")
        self.loadBoundaryCoord(fileNames)
        self.drawBoundaryCoord()
        self.initLines()
        self.startAnim()


test1 = plot_manager()
test = zbPeristalsis(test1.getFigure(),gf.generateFrameSet("*.tif"),None)

