import seaborn as sb

from plotmanager.plottype import animPlot


class Violin(animPlot.AnimPlot):

    def __init__(self,figure, data, plot_XML):
        animPlot.AnimPlot.__init__(self,figure, data, plot_XML)
        self.type = "violin"
        self.violinPlot = 0
        return

    def animate(self,i):
        return

    def draw(self):

        if(len(self.data.get().columns)==3):
            self.violinPlot = sb.violinplot(x=self.data.get().iloc[:, 0], y=self.data.get().iloc[:, 1],hue=self.data.get().iloc[:, 2],split=True,ax=self.subplot)
        else:
            self.violinPlot = sb.violinplot(x=self.data.get().iloc[:,0],y=self.data.get().iloc[:,1],ax=self.subplot)


        return

    def initAnimate(self, i):
        return

