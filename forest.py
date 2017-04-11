
import animPlot as animPlot
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#data format:  [Label,Odds Ratio,Lower Confidence Interval, Upper Confidence Interval]
class forest(animPlot.animPlot):

    def __init__(self, figure, data, position,title="",plotArgs=[],annotate=[]):
        animPlot.animPlot.__init__(self, figure, data, position,title,plotArgs,annotate)

        #self.initializeForest()

        return
    def draw(self):

        plt.axvline(x=1.0,linewidth=1.5,color="black", alpha=0.5,axes=self.subplot, dashes=[2,1])

        Y = np.arange(len(self.data.index))

        self.subplot.plot(self.data.ix[:, 2], Y, "rh",markersize=15)

        self.subplot.set_yticks(Y)
        self.subplot.yaxis.grid(b=False)
        self.subplot.xaxis.grid(b=True)

        secondaryAxis = self.subplot.twinx()
        secondaryAxis.set_yticks(Y)

        secondaryAxis.set_ylim(self.subplot.get_ylim())

        secondaryAxis.set_yticklabels(self.data.ix[:, 2].round(2))

        secondaryAxis.grid(b=False)
        self.subplot.set_xlim([0, 200])
        self.subplot.set_yticklabels(self.data.ix[:, 0])
        self.subplot.set_xlabel("Odds Ratio")

        for index, row in self.data.iterrows():
            yCoord = [Y[index], Y[index]]
            self.subplot.plot(row[3:5], yCoord, "r-")

            if self.retrieveArgVal("showP") is not None:
                plt.annotate("$\it{p}$ = " + str.format("{0:.5f}",row[5]),[row[2],Y[index]],xytext=[10,-20],textcoords="offset points",bbox=dict(boxstyle="round",
                            fc=(1.0, 0.7, 0.7),
                            ec=(1., .5, .5)),
                            arrowprops=dict(arrowstyle="wedge,tail_width=1.",
                            fc=(1.0, 0.7, 0.7), ec=(1., .5, .5),
                            patchA=None,
                            patchB=None,
                            relpos=(0.2, 0.8),
                            connectionstyle="arc3,rad=-0.1"))

        return
    def initAnimate(self):
        print(0)
        return
    def animate(self):
        print(0)
        return
    def initializeForest(self):

        return

