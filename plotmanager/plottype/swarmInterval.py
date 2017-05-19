from plotmanager.plottype import animPlot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.collections as collect
import matplotlib.patches as patches



class swarmInterval(animPlot.animPlot):

    def __init__(self,figure,data,position, title="",plotArgs=[],annotate=[]):
        animPlot.animPlot.__init__(self,figure,data,position,title,plotArgs,annotate)
        self.ID = self.data.ix[:,0]
        self.value = self.data.ix[:,1]
        self.interval = self.data.ix[:,2]
        self.intervalPatches = []
        self.midPtLines = []
        self.patchCollection = []
        self.midPtLineCollection = []

    def draw(self):


        X = np.arange(0,((len(self.value))*2)+1)

        self.subplot.plot(X[1::2],self.value,"rh",markersize=5,color="#9F4298")

        for i, x in enumerate(self.interval):

            if isinstance(x,str):


                if x[0] != ">" and x[0] != "<":
                    limits = x.split("-")
                    xrect = (i*2)
                    newRect = patches.Rectangle((xrect,float(limits[0])),2,float(limits[1])-float(limits[0]))
                    midpoint = float(limits[0]) + (float(limits[1])-float(limits[0]))/2
                    newMidptLine = [(xrect,midpoint),(xrect+2,midpoint)]
                    self.midPtLines.append(newMidptLine)
                    self.intervalPatches.append(newRect)


        self.patchCollection = collect.PatchCollection(self.intervalPatches, facecolor="#e9e7e8",alpha=0.9)
        self.patchCollection.set_alpha(0.9)
        self.midPtLineCollection = collect.LineCollection(self.midPtLines,colors="#c1bdbe",alpha=0.9)
        self.midPtLineCollection.set_alpha(0.9)
        self.subplot.add_collection(self.patchCollection)
        self.subplot.add_collection(self.midPtLineCollection)

        self.subplot.set_xticks(X[1::2])

        if self.showXlabels != False: self.subplot.set_xticklabels(self.ID)

        self.subplot.semilogy()


        return


    def initAnimate(self):
        return
    def animate(self):
        return