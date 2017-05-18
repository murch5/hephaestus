import plot_class.plot as plot
import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np




import scipy.spatial.distance as sp_spatial_distance
import scipy.cluster.hierarchy as sp_cluster_hierarchy

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

        if self.retrieveArgVal("SaveHierarchyClust") is not None:
            data = self.data.T
            pairwiseDist = sp_spatial_distance.pdist(data)
            self.clusterHierarchy = sp_cluster_hierarchy.linkage(pairwiseDist,method="complete")
            self.clusterHierarchy.dump("process_data/hierarchy/cluster/"+ str(self.retrieveArgVal("SaveHierarchyClust")) + ".cluster")

        if self.retrieveArgVal("GetHierarchyClust") is not None:
            self.clusterHierarchy = np.load(
                "process_data/hierarchy/cluster/" + str(self.retrieveArgVal("GetHierarchyClust")) + ".cluster")

        print(self.clusterHierarchy.shape)

        self.clusterMap = sb.clustermap(self.data,col_linkage=self.clusterHierarchy,vmin=self.vmin,vmax=self.vmax, figsize=(25,12))

        plt.setp(self.clusterMap.ax_heatmap.get_yticklabels(), rotation=0)
        plt.setp(self.clusterMap.ax_heatmap.get_xticklabels(), rotation=90)

        if self.retrieveArgVal("hideXlabel") is not None:
            self.clusterMap.ax_heatmap.xaxis.set_visible(False)
        if self.retrieveArgVal("hideYlabel") is not None:
            self.clusterMap.ax_heatmap.yaxis.set_visible(False)

        self.clusterMap.savefig(self.plotTitle + ".png")

        return;

    def __init__(self,figure, data, position,title="",plotArgs=[],annotate=[]):
        plot.plot.__init__(self,figure, data, position,title,plotArgs,annotate)
        self.position = position
        self.fig = figure
        self.clusterMap = 0
        self.vmin = 0
        self.vmax = 100
        self.clusterHierarchy = 0

        self.data.set_index("GeneName",inplace=True)

        print(self.data)

    def initAnimate(self, i):
        return;
