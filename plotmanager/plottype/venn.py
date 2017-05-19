#Using matplotlib-venn library

import matplotlib_venn as plotvenn
from plotmanager.plottype import plot


class venn(plot.plot):

    def animate(self,i):
        return;

    def draw(self):

        if self.groups == 2:
            set1 = set(self.data.ix[:,0])
            set2 = set(self.data.ix[:,1])
            setNames = self.data.columns.values.tolist()
            self.venn = plotvenn.venn2([set1,set2],ax=self.subplot, set_labels=setNames)
        elif self.groups == 3:
            set1 = set(self.data.ix[:, 0])
            set2 = set(self.data.ix[:, 1])
            set3 = set(self.data.ix[:, 1])
            setNames = self.data.columns.values.tolist()
            self.venn = plotvenn.venn3([set1, set2,set3],ax=self.subplot, set_labels=setNames)

        return;

    def __init__(self,figure, data, position,title="",plotArgs=[],annotate=[]):
        plot.plot.__init__(self,figure, data, position,title,plotArgs,annotate)
        self.position = position
        self.fig = figure
        self.groups = len(self.data.columns)
        self.venn = 0

    def initAnimate(self, i):
        return;
