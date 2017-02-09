import animPlot as animPlot
import seaborn as sb


class violin(animPlot.animPlot):

    def __init__(self, figure, data, position , title="",plotArgs=[]):
        animPlot.animPlot.__init__(self, figure, data, position,title,plotArgs)
        self.violinPlot = 0
        return

    def animate(self,i):
        return

    def draw(self):

        if(len(self.data.columns)==3):
            self.violinPlot = sb.violinplot(x=self.data.iloc[:, 0], y=self.data.iloc[:, 1],hue=self.data.iloc[:, 2],split=True,ax=self.subplot)
        else:
            self.violinPlot = sb.violinplot(x=self.data.iloc[:,0],y=self.data.iloc[:,1],ax=self.subplot)

            #self.violinPlot = sb.violinplot(data=self.data, ax=self.subplot)


        return

    def initAnimate(self, i):
        return

