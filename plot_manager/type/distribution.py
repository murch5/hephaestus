import seaborn as sb
import matplotlib.pyplot as plt

from type import anim_plot


class Distribution(anim_plot.AnimPlot):
    def draw(self):

        self.subplot = sb.distplot(self.data[0].ix[:, 0], hist_kws=dict(edgecolor="k", linewidth=1))
        #self.subplot.set_xscale("log")

        self.subplot.yaxis.grid(True)

        plt.rcParams["font.size"] = 36
        plt.rcParams["xtick.labelsize"] = 36
        plt.rcParams["ytick.labelsize"] = 36
        plt.rcParams["axes.labelsize"] = 36

        #context = sb.set_context(font_scale=1.5, rc={"font.size": 16, "xtick.labelsize": 16,
          #  "ytick.labelsize": 16, "axes.labelsize":32})
        return
