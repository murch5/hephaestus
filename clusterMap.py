import plot as plot
import seaborn as sb
import matplotlib.pyplot as plt


import sys
sys.setrecursionlimit(40000)

class clusterMap(plot.plot):

    def animate(self,i):
        return;

    def draw(self):

        if self.retrieveArgVal("vmin") is not None:
            self.vmin = int(self.retrieveArgVal("vmin"))
        if self.retrieveArgVal("vmax") is not None:
            self.vmax = int(self.retrieveArgVal("vmax"))

        print(self.vmin)
        print(self.vmax)
        self.clusterMap = sb.clustermap(self.data,method="average",row_cluster=True,vmin=self.vmin,vmax=self.vmax, figsize=(25,12))

        plt.setp(self.clusterMap.ax_heatmap.get_yticklabels(), rotation=0)
        plt.setp(self.clusterMap.ax_heatmap.get_xticklabels(), rotation=90)

        if self.retrieveArgVal("hideXlabel") is not None:
            self.clusterMap.ax_heatmap.xaxis.set_visible(False)
        if self.retrieveArgVal("hideYlabel") is not None:
            self.clusterMap.ax_heatmap.yaxis.set_visible(False)

        #self.clusterMap.savefig("test1.png")

        return;

    def __init__(self,figure, data, position,title="",plotArgs=[],annotate=[]):
        plot.plot.__init__(self,figure, data, position,title,plotArgs,annotate)
        self.position = position
        self.fig = figure
        self.clusterMap = 0
        self.vmin = 0
        self.vmax = 100

        self.data.set_index("GeneName",inplace=True)

        print(self.data)

    def initAnimate(self, i):
        return;
