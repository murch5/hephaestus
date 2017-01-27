import animPlot as animPlot
import numpy as np

class pie(animPlot.animPlot):

    def __init__(self, figure, data, position, title="", explode=0):
        animPlot.animPlot.__init__(self, figure, data, position,title)
        self.explode = explode
        self.NaNindices = self.data.isnull()
        self.numNan = np.sum(self.NaNindices)
        self.dataCleaned = self.data[self.data.notnull()]

        print(self.dataCleaned)
        return

    def animate(self,i):
        return

    def draw(self):

        def my_autopct(pct):
            return ('%.2f' % pct) if pct > 1 else ''

        if self.explode != 0:
            self.subplot.pie(self.dataCleaned,labels=list(self.dataCleaned.index), startangle=90, explode=self.explode, autopct=my_autopct)
        else:
            self.subplot.pie(self.dataCleaned, labels=list(self.dataCleaned.index), startangle=90,autopct=my_autopct)

        self.subplot.axis("equal")

        return

    def initAnimate(self, i):
        return

