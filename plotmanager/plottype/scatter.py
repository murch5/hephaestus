import seaborn as sb

from plotmanager.plottype import animPlot


class scatter(animPlot.animPlot):

    def __init__(self,figure,data,position, title="",plotArgs=[],annotate=[]):
        animPlot.animPlot.__init__(self,figure,data,position,title,plotArgs,annotate)


    def draw(self):

        sb.regplot(x=self.data.ix[:,0],y=self.data.ix[:, 1],fit_reg=True,ax=self.subplot)

    def initAnimate(self):
        print(0)
    def animate(self):
        print(0)