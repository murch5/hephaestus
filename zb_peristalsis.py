import contourMapAnim as cm
import generateFrameSet as gf
import numpy as np
from matplotlib import lines as ln
import matplotlib.collections as collect

class zbPeristalsis():

    def drawLines(self):

        for boundaryLines in self.lineCoord:
            print(boundaryLines)
            print(type(boundaryLines))
            print(boundaryLines.shape)
            print(boundaryLines[:,0])
           # lines = np.concatenate(boundaryLines[:,0],boundaryLines[:,1])
            self.lineCollection = collect.LineCollection(boundaryLines[[]])
            print(self.lineCollection)
          #  self.contourAnimationHandler.subplot.add_line(ln.Line2D(boundaryLines[:,0],boundaryLines[:,1]))
        return;

    def initLines(self):

        return;
    def loadBoundaryCoord(self,fileNames):

        for file in fileNames:
            print(file)
            d = np.loadtxt(file)
            print(d)
            self.lineCoord.append(np.loadtxt(file,dtype=int,delimiter="\t"))

        return;

    def drawBoundaryCoord(self):
        self.contourAnimationHandler.contourMapBase.assignLineDrawFunc(self.drawLines)

        return;

    def __init__(self):
        self.contourAnimationHandler = cm.contourMapAnim(gf.generateFrameSet("*.tif"))
        self.lineCoord = []
        self.lineCollection = None

        fileNames = []

        fileNames.append("Bottom.txt")
        fileNames.append("Top.txt")
        self.loadBoundaryCoord(fileNames)
        self.drawBoundaryCoord()

        self.contourAnimationHandler.startAnim()



test = zbPeristalsis()

