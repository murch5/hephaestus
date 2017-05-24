#Using matplotlib-venn library

import matplotlib_venn as plotvenn
from plotmanager.plottype import plot

class Venn(plot.Plot):

    def animate(self,i):
        return

    def draw(self):

        if self.groups == 2:
            set1 = set(self.data[0].get().ix[:,0])
            set2 = set(self.data[0].get().ix[:,1])
            setNames = self.data[0].get().columns.values.tolist()
            self.venn = plotvenn.venn2([set1,set2],ax=self.subplot, set_labels=setNames)
        elif self.groups == 3:
            set1 = set(self.data[0].get().ix[:, 0])
            set2 = set(self.data[0].get().ix[:, 1])
            set3 = set(self.data[0].get().ix[:, 2])
            setNames = self.data[0].get().columns.values.tolist()
            self.venn = plotvenn.venn3([set1, set2,set3],ax=self.subplot, set_labels=setNames)

        return;

    def __init__(self,figure, data, plot_XML):
        plot.Plot.__init__(self,figure, data, plot_XML)
        self.fig = figure
        self.groups = len(self.data[0].get().columns)
        self.venn = 0

    def initAnimate(self, i):
        return;
