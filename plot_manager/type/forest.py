from type import anim_plot
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#data format:  [Label,Odds Ratio,Lower Confidence Interval, Upper Confidence Interval]
class Forest(anim_plot.AnimPlot):

    def draw(self):

        #plt.axvline(x=1.0,linewidth=1.5,color="black", alpha=0.5,axes=self.subplot, dashes=[2,1])

        color_wedge = ["#2D75A2", "#E0812B"]

        Y = np.arange(len(self.data[0].index))

        self.subplot.plot(self.data[0].ix[:, 3], Y, "rh",markersize=20, color=color_wedge[1], lw=1,markeredgecolor="black")

        self.subplot.set_yticks(Y)
        self.subplot.yaxis.grid(b=False)
        self.subplot.xaxis.grid(b=True)

        secondary_axis = self.subplot.twinx()
        secondary_axis.set_yticks(Y)

        secondary_axis.set_ylim(self.subplot.get_ylim())

        secondary_axis.set_yticklabels(self.data[0].ix[:, 3].round(2))

        secondary_axis.grid(b=False)
        self.subplot.set_xlim([self.vmin, self.vmax])
        self.subplot.set_yticklabels(self.data[0].ix[:, 1])
        self.subplot.set_xlabel("Odds Ratio")

        for index, row in self.data[0].iterrows():
            yCoord = [Y[index], Y[index]]
            self.subplot.plot(row[4:6], yCoord, "r-", color = color_wedge[1])

            if self.get("show_p_value"):
                self.subplot.annotate("$\it{p}$ = " + str.format("{0:.3f}", row[8]), [row[3], Y[index]], xytext=[10, -20],
                         textcoords="offset points", bbox=dict(boxstyle="round",
                                                               alpha=0.60,
                                                               fc=color_wedge[0],
                                                               ec=(1., .5, .5)))

        #self.subplot.set_xscale('semilog')

        self.subplot.axvline(x=1.000, color='b', linestyle='--')

        return

