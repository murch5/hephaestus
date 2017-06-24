import seaborn as sb

from plot_manager.type import anim_plot


class Scatter(anim_plot.AnimPlot):

    def draw(self):

        sb.regplot(x=self.data[0].ix[:,0],y=self.data[0].ix[:, 1],fit_reg=True,ax=self.subplot)

        pass