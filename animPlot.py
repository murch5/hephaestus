import plot as plot

class animPlot(plot.plot):

    def animate(self,i):
        return;

    def draw(self):
        return;

    def __init__(self,figure, data, position):
        plot.plot.__init__(self,figure, data, position)

    def initAnimate(self, i):
        return;
