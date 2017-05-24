from plotmanager.plottype import plot


class AnimPlot(plot.Plot):

    def animate(self,i):
        return;

    def draw(self):
        return;

    def __init__(self,figure, data, plot_XML):
        plot.Plot.__init__(self,figure, data, plot_XML)

    def initAnimate(self, i):
        return;
