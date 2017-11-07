import seaborn as sb

from plot_manager.type import anim_plot


class Scatter(anim_plot.AnimPlot):

    def draw(self):

        #self.subplot = sb.regplot(x=self.data[0].ix[:,0],y=self.data[0].ix[:, 1],fit_reg=False,ax=self.subplot, scatter_kws={"color":self.data[0].ix[:, 1]})

        #scatter = self.subplot.scatter(x=self.data[0].ix[:,0],y=self.data[0].ix[:, 1], c=self.data[0].ix[:, 2])


        lmplot = sb.lmplot(x=self.data[0].ix[:,0].name,y=self.data[0].ix[:, 1].name,data=self.data[0],fit_reg=False, hue=self.data[0].ix[:,2].name, legend_out=True)

        lmplot.fig.set_size_inches(12,12)
        self.figure = lmplot.fig

        pass