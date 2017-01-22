import animPlot as animPlot
import seaborn as sb

class scatter(animPlot.animPlot):

    def __init__(self,figure,data,position):


    def draw(self):
        sb.plt(sb.plt.scatter,x=self.data.iloc[:, 1],y=self.data.iloc[:, 2])


    def initAnimate(self):
        print(0)
    def animate(self):
        print(0)