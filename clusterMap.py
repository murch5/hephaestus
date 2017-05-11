import plot as plot
import seaborn as sb
import matplotlib.pyplot as plt


import sys
sys.setrecursionlimit(40000)

class clusterMap(plot.plot):

    def animate(self,i):
        return;

    def draw(self):

        self.clusterMap = sb.clustermap(self.data,method="average",row_cluster=True,vmin=0,vmax=300, figsize=(25,12))

        plt.setp(self.clusterMap.ax_heatmap.get_yticklabels(), rotation=0)
        plt.setp(self.clusterMap.ax_heatmap.get_xticklabels(), rotation=90)

        self.clusterMap.ax_heatmap.xaxis.set_visible(False)
        self.clusterMap.ax_heatmap.yaxis.set_visible(False)

        self.clusterMap.savefig("test1.png")
        return;

    def __init__(self,figure, data, position,title="",plotArgs=[],annotate=[]):
        plot.plot.__init__(self,figure, data, position,title,plotArgs,annotate)
        self.position = position
        self.fig = figure
        self.clusterMap = 0

        self.data.set_index("GeneName",inplace=True)

        print(self.data)

    def initAnimate(self, i):
        return;
