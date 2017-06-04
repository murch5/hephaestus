import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import matplotlib.patches as patches
import matplotlib.collections as collect

from plotmanager.plottype import plot


class Track(plot.Plot):

    def __init__(self,figure, data, plot_settings):
        plot.Plot.__init__(self,figure, data, plot_settings)
        self.chainLimits = []
        self.features = []
        self.featurePatches = []
        self.featurePatchesCollection = []
        self.featureMidpts = []
        self.featureLabel = ""
        self.featureLabelList = []



        return

    def animate(self,i):
        return;

    def draw(self):

        chain = self.subplot.plot([self.chainLimits[0],self.chainLimits[1]], [1,1], "b-", zorder=0)

        for index, row in self.features.iterrows():

            featureStart = row["start"]
            featureEnd = row["end"]
            midpt = featureStart + ((featureEnd - featureStart) / 2)
            self.featureMidpts.append(midpt)
            length = featureEnd-featureStart

            newRect = patches.Rectangle((featureStart, 0.75), length, 0.5)
            self.featurePatches.append(newRect)
            self.featureLabelList.append(row["attrDict"].get(self.featureLabel))
           # self.subplot.annotate(s=row["attrDict"].get("Note"), xy=(midpt,0.60), xycoords="data",
                     #                        color="black",horizontalalignment='center')
#
        colorWedge = ["#9F4298", "#D1AFD3"]
        self.featurePatchesCollection = collect.PatchCollection(self.featurePatches,color=colorWedge,zorder=1)
        self.subplot.add_collection(self.featurePatchesCollection)

        self.trackAnnotations()

        self.subplot.set_ylim([0.5,1.5])
        self.subplot.title.set_text("")
        self.subplot.axis("off")

        return;

    def trackAnnotations(self):

        labels = self.data.getDictValues(self.featureLabel)

        for i, x in enumerate(self.featureMidpts):

            self.subplot.annotate(s=self.featureLabelList[i], xy=(x, 0.60), xycoords="data",
                                  color="black", horizontalalignment='center')

        return