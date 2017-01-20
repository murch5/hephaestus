import animPlot as animPlot
import seaborn as sb


class violin(animPlot.animPlot):

    def __init__(self, figure, data, position):
        animPlot.animPlot.__init__(self, figure, data, position)
        self.violinPlot = 0
        return

    def animate(self,i):
        return

    def draw(self):
        print("test")
        print(self.getData)
        self.violinPlot = sb.violinplot(x=self.data[0],y=self.data[1],ax=self.subplot)

        return

    def initAnimate(self, i):
        return

