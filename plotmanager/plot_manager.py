import matplotlib.animation as anim
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb
from plotmanager.plottype.DNAtrack import DNAtrack
from plotmanager.plottype.clusterMap import clusterMap
from plotmanager.plottype.contourMap import contourMap
from plotmanager.plottype.forest import forest
from plotmanager.plottype.imageStack import imageStack
from plotmanager.plottype.pie import pie
from plotmanager.plottype.proteinTrack import proteinTrack
from plotmanager.plottype.scatter import scatter
from plotmanager.plottype.survival import survival
from plotmanager.plottype.swarmInterval import swarmInterval
from plotmanager.plottype.track import track
from plotmanager.plottype.variantTrack import variantTrack
from plotmanager.plottype.venn import venn
# from plottype.imageStack import imageStack
from plotmanager.plottype.violin import violin
from plotmanager.plottype.zb_peristalsis import zbPeristalsis

from plotmanager.plottype.image import image

plt.rcParams['animation.ffmpeg_path'] = '/ffmpeg/bin/ffmpeg'
plt.rcParams['image.cmap'] = 'magma'

chartTypes = {"violin": violin, "pie": pie, "scatter": scatter, "forest": forest, "contour": contourMap,
              "imageStack": imageStack, "zbperistalsis": zbPeristalsis, "image": image, "swarmInterval": swarmInterval,
              "survival": survival, "track": track, "proteinTrack": proteinTrack, "DNAtrack": DNAtrack,
              "variantTrack": variantTrack, "clusterMap": clusterMap, "venn": venn}
funcTypes = {"sum": sum}


class plot_manager():
    def __init__(self, name, figureArgs):
        self.name = name
        self.figure = plt.figure(figsize=(11, 9))
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
        self.figArgList = self.parseArgs(figureArgs)

        self.currentView = 0

        # self.cid = self.figure.canvas.mpl_connect('resize_event', self.onResize)
        # if self.retrieveArgVal("hideTitle") is not None: self.figure.suptitle("")
        # else:   self.figure.suptitle(self.name)


        self.setStyleSheet("seaborn-pastel")

        self.evaluateFigureArgs()

        return

    def onResize(self, event):
        print("Resizing...")
        self.drawPlots()
        self.figure.canvas.flush_events()
        return

    def parseViewSet(self, fileName):

        viewSetCoding = pd.read_csv(fileName, sep=",")

        return

    def addView(self, viewTitle):

        newView = []
        self.viewList.append(newView)
        self.viewLabels.append(viewTitle)

        return

    def addPlot(self, title, position, plotClass, data, plotArgs, annotate):
        newPlot = plotClass(self.figure, data, position, title, plotArgs, annotate)
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

        # vidFileName = "View_" + self.
        self.writer = anim.FFMpegWriter(fps=15, bitrate=5000)
        self.animHandler.save("t.mp4", writer=self.writer)
        return

    def initAnim(self):

        return

    def animatePlot(self, i):

        for plot in self.plotList:
            plot.animate(i)
            plot.annotate()
        return

    def getFigure(self):
        return self.figure

    def addLabel(self, text, position, colorMap, index):
        self.plotList[index].addTextAnnotation(text, position, colorMap)
        return

    def drawPlots(self):

        for plot in self.plotList:
            plot.draw()
            plot.annotate()

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

    def parseArgs(self, args):

        argPD = pd.Series(args)
        argList = []
        if argPD.any():
            for i in argPD:

                if i != 0:
                    q = i.split("=", 1)
                    argList.append(q)

        if (len(argList) > 0):

            if argList[0][0] != "0":
                argList = dict(argList)
                self.argFlag = True
            else:
                argList = {0: 0}
        else:
            argList = {0: 0}

        return argList

    def retrieveArgVal(self, argID):

        return self.figArgList.get(argID)

    def evaluateFigureArgs(self):

        if self.retrieveArgVal("hideTitle") is not None:
            self.figure.suptitle("")

        return
