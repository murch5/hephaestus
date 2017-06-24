import seaborn as sb

from plot_manager.plottype import anim_plot

class Violin(anim_plot.AnimPlot):

    def draw(self):

        if(len(self.data[0].columns)==3):
            self.violinPlot = sb.violinplot(x=self.data[0].iloc[:, 0], y=self.data[0].iloc[:, 1],hue=self.data[0].iloc[:, 2],split=True,ax=self.subplot)
        else:
            self.violinPlot = sb.violinplot(x=self.data[0].iloc[:,0],y=self.data[0].iloc[:,1],ax=self.subplot)

        return

