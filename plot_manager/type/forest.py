from plot_manager.type import anim_plot
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#data format:  [Label,Odds Ratio,Lower Confidence Interval, Upper Confidence Interval]
class Forest(anim_plot.AnimPlot):

    def __init__(self,figure, data, plot_settings):
        anim_plot.AnimPlot.__init__(self, figure, data, plot_settings)

        #self.initializeForest()

        return
    def draw(self):

        plt.axvline(x=1.0,linewidth=1.5,color="black", alpha=0.5,axes=self.subplot, dashes=[2,1])

        Y = np.arange(len(self.data.get().index))

        self.subplot.plot(self.data.get().ix[:, 2], Y, "rh",markersize=15)

        self.subplot.set_yticks(Y)
        self.subplot.yaxis.grid(b=False)
        self.subplot.xaxis.grid(b=True)

        secondary_axis = self.subplot.twinx()
        secondary_axis.set_yticks(Y)

        secondary_axis.set_ylim(self.subplot.get_ylim())

        secondary_axis.set_yticklabels(self.data.ix[:, 2].round(2))

        secondary_axis.grid(b=False)
        self.subplot.set_xlim([0, 200])
        self.subplot.set_yticklabels(self.data.get().ix[:, 0])
        self.subplot.set_xlabel("Odds Ratio")

        for index, row in self.data.get().iterrows():
            yCoord = [Y[index], Y[index]]
            self.subplot.plot(row[3:5], yCoord, "r-")

            #if self.retrieveArgVal("showP") is not None:
             #   plt.annotate("$\it{p}$ = " + str.format("{0:.5f}",row[5]),[row[2],Y[index]],xytext=[10,-20],textcoords="offset points",bbox=dict(boxstyle="round",
              #              fc=(1.0, 0.7, 0.7),
             #               ec=(1., .5, .5)),
              #              arrowprops=dict(arrowstyle="wedge,tail_width=1.",
              #              fc=(1.0, 0.7, 0.7), ec=(1., .5, .5),
              #              patchA=None,
              #              patchB=None,
               #             relpos=(0.2, 0.8),
               #             connectionstyle="arc3,rad=-0.1"))

        return

