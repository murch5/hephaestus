#Using matplotlib-venn library

import matplotlib_venn as plotvenn
from plot_manager.type import plot

class Venn(plot.Plot):

    def draw(self):

        self.groups = len(self.data[0].columns)

        if self.groups == 2:
            set1 = set(self.data[0].ix[:,0])
            set2 = set(self.data[0].ix[:,1])
            set_names = self.data[0].columns.values.tolist()
            self.venn = plotvenn.venn2([set1,set2],ax=self.subplot, set_labels=set_names)
        elif self.groups == 3:
            set1 = set(self.data[0].ix[:, 0])
            set2 = set(self.data[0].ix[:, 1])
            set3 = set(self.data[0].ix[:, 2])
            set_names = self.data[0].columns.values.tolist()
            self.venn = plotvenn.venn3([set1, set2,set3],ax=self.subplot, set_labels=set_names)

        return


    def initialize(self):
        self.groups = None
