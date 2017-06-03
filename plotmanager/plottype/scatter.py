import seaborn as sb

from plotmanager.plottype import anim_plot


class Scatter(anim_plot.AnimPlot):

    def __init__(self,figure, data, plot_XML):
        anim_plot.AnimPlot.__init__(self, figure, data, plot_XML)


    def draw(self):

        sb.regplot(x=self.data.get().ix[:,0],y=self.data.get().ix[:, 1],fit_reg=True,ax=self.subplot)

    def initAnimate(self):
        print(0)
    def animate(self):
        print(0)