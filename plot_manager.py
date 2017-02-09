
import matplotlib.pyplot as plt
from imageStack import imageStack
from violin import violin
from pie import pie
from scatter import scatter
from forest import forest
from contourMap import contourMap
import generateFrameSet as gf
import matplotlib.animation as anim
import pandas as pd
import seaborn as sb

plt.rcParams['animation.ffmpeg_path'] = '/ffmpeg/bin/ffmpeg'
plt.rcParams['image.cmap'] = 'gray'

chartTypes = {"violin":violin,"pie":pie,"scatter":scatter, "forest":forest, "contour":contourMap}
funcTypes = {"sum":sum}

class plot_manager():
    def __init__(self, name):
        self.name = name
        self.figure = plt.figure(figsize=(10, 8))
        self.plotList = []
        self.viewList = []
        self.viewLabels = []
        self.animHandler = None
        self.writer = None
        self.framesPerImage = 1
        self.totalFrames = 80
        self.currFrameIndex = 0
        self.currImageIndex = 0
        self.saveAnimFlag = False

        self.currentView = 0

        self.figure.suptitle(self.name)

        self.setStyleSheet("seaborn-pastel")

        return;

    def parseViewSet(self, fileName):

        viewSetCoding = pd.read_csv(fileName, sep=",")

        return

    def addView(self, viewTitle):

        newView = []
        self.viewList.append(newView)
        self.viewLabels.append(viewTitle)

        return

    def addPlot(self,title, position, plotClass, data, plotArgs):
        newPlot = plotClass(self.figure, data, position, title, plotArgs)
        self.plotList.append(newPlot)

    def addPlotToView(self, plotClass, data, position, viewID):
        newPlot = plotClass(self.figure, data, position)
        self.viewList[viewID].append(newPlot)

    def startAnim(self):
        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')
        self.saveAnimFlag = True
        self.animHandler = anim.FuncAnimation(self.figure, self.animatePlot,
                                              frames=self.framesPerImage * self.totalFrames, init_func=self.initAnim)
        if self.saveAnimFlag == True: self.saveAnimationToFile()
        plt.show()
        return

    def saveAnimationToFile(self):

        self.writer = anim.FFMpegWriter(fps=15, bitrate=5000)
        self.animHandler.save("t.mp4", writer=self.writer)
        return

    def initAnim(self):

        return

    def animatePlot(self, i):

        for plot in self.plotList:
            plot.animate(i)
            plot.drawText()
        return

    def getFigure(self):
        return self.figure

    def addLabel(self, text, position, colorMap, index):
        self.plotList[index].addTextAnnotation(text, position, colorMap)
        return

    def drawPlots(self):

        for plot in self.plotList:
            plot.draw()

        return

    def drawView(self):


        currView = self.viewList[self.currentView]

        for plot in currView:
            plot.draw()

        return

    def setView(self, newView):
        self.currentView = newView
        return

    def captureImage(self, style):

        if style == "PDF":
            self.figure.savefig(self.name + ".pdf")
        if style == "PNG":
            self.figure.savefig(self.name + ".png")
        if style == "Both":
            self.figure.savefig(self.name + ".pdf")
            self.figure.savefig(self.name + ".png")

    def setStyleSheet(self, styleSheet):
        plt.style.use(styleSheet)
        sb.set_style("white")
        sb.set_style("ticks")
        sb.despine()

    def showPlot(self):

        plt.show()


# test1.addPlot(violin,((1,2,2,2,1,1,1),(2,2,3,2,4,6,2)),212)
# test1.drawPlots()
