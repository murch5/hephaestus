import seaborn as sb
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import ticker

from type import anim_plot


class Scatter(anim_plot.AnimPlot):

    def draw(self):

        print(self.data[0])
        # self.subplot = sb.regplot(x=self.data[0].ix[:,0],y=self.data[0].ix[:, 1],fit_reg=False,ax=self.subplot, scatter_kws={"color":self.data[0].ix[:, 1]})

        # scatter = self.subplot.scatter(x=self.data[0].ix[:,0],y=self.data[0].ix[:, 1], c=self.data[0].ix[:, 2])

       # lmplot = sb.lmplot(x=self.data[0].ix[:, 0].name, y=self.data[0].ix[:, 1].name, data=self.data[0], fit_reg=False,
        #                   hue=self.data[0].ix[:, 2].name, palette=sb.color_palette("muted"), legend=self.show_legend, legend_out=True)


        if self.get("show_hue") == False:

            lmplot = sb.lmplot(x=self.data[0].ix[:, 0].name, y=self.data[0].ix[:, 1].name, data=self.data[0], fit_reg=False,
                           palette=sb.color_palette("muted"), legend=self.show_legend,
                           legend_out=True, scatter_kws={"s": 10})
        else:

            lmplot = sb.lmplot(x=self.data[0].ix[:, 0].name, y=self.data[0].ix[:, 1].name, data=self.data[0],
                               fit_reg=False, hue=self.data[0].ix[:, 2].name,
                               palette=sb.color_palette("muted"), legend=None,
                               legend_out=True, scatter_kws={"s": 10})





        self.figure = lmplot.fig

        #plt.rcParams.update({"font.size": 2,"xtick.labelsize": 2, "axes.labelsize":2})
        #plt.rcParams["xtick.labelsize"] = 16
        #plt.rcParams["ytick.labelsize"] = 16
        #plt.rcParams["axes.labelsize"] = 16
        print(lmplot.ax)
        print(lmplot.axes)
        #lmplot.ax.xaxis.set_major_locator(ticker.AutoLocator())
        #lmplot.ax.yaxis.set_major_locator(ticker.AutoLocator())

        lmplot.ax.xaxis.label.set_size(16)
        lmplot.ax.yaxis.label.set_size(16)

        lmplot.ax.tick_params(axis='both', which='major', labelsize=12)

        sb.set_context(font_scale=0.25, rc={"font.size": 2, "xtick.labelsize": 2,
          "ytick.labelsize": 2, "axes.labelsize":2})
        pass
