import animPlot as animPlot
import seaborn as sb
import matplotlib as plt

class scatter(animPlot.animPlot):

    def __init__(self,figure,data,position):
        animPlot.animPlot.__init__(self,figure,data,position)
        print(0)

    def draw(self):
        sb.regplot(x=self.data.iloc[:,0],y=self.data.iloc[:, 1],fit_reg=False,ax=self.subplot)

    def initAnimate(self):
        print(0)
    def animate(self):
        print(0)