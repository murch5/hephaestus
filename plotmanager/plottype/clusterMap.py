from plotmanager.plottype import plot
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np
import glob as glob
import os as os

import scipy.spatial.distance as sp_spatial_distance
import scipy.cluster.hierarchy as sp_cluster_hierarchy

import sys

sys.setrecursionlimit(40000)

class ClusterMap(plot.Plot):
    def animate(self, i):
        return

    def draw(self):

        if self.checkXML(".//plot_style//vmin"):
            self.vmin = self.getXMLvalue(".//plot_style//vmin")
        if self.checkXML(".//plot_style//vmax"):
            self.vmax = self.getXMLvalue(".//plot_style//vmax")

        if self.checkXML(".//plot_style//save_hierarchy_clust"):
            data_transpose = self.data.get().T
            pairwise_dist = sp_spatial_distance.pdist(data_transpose)
            self.clusterHierarchy = sp_cluster_hierarchy.linkage(pairwise_dist, method="complete")
            clusterNameOutput = str(self.plot_XML.find(".//plot_style//save_hierarchy_clust").text) + ".cluster"
            clusterOutputPath = os.path.join("./process/hierarchy/cluster/", clusterNameOutput)
            self.clusterHierarchy.dump(clusterOutputPath)

        if self.checkXML(".//plot_style//get_hierarchy_clust"):
            clusterinput_name = str(self.plot_XML.find(".//plot_style//get_hierarchy_clust").text) + ".cluster"
            clusterinput_path = os.path.join("./process/hierarchy/cluster/", clusterinput_name)
            self.clusterHierarchy = np.load(clusterinput_path)

        if self.checkXML(".//plot_style//std_scale"):
            self.standard_scale = self.getXMLvalue(".//plot_style//std_scale")

        if self.checkXML(".//plot_style//z_score"):
            self.z_score = self.getXMLvalue(".//plot_style//z_score")

        if self.checkXML(".//plot_style//fig_size"):
            self.z_score = self.getXMLvalue(".//plot_style//fig_size")


        self.cluster_map = sb.clustermap(self.data[0].get(), col_linkage=self.clusterHierarchy, vmin=self.vmin,
                                         vmax=self.vmax, standard_scale=self.standard_scale, z_score=self.z_score,
                                         figsize=(25, 12))

        plt.setp(self.cluster_map.ax_heatmap.get_yticklabels(), rotation=0)
        plt.setp(self.cluster_map.ax_heatmap.get_xticklabels(), rotation=90)

        if self.checkXML(".//plot_style//hide_xlabel"):
            self.cluster_map.ax_heatmap.xaxis.set_visible(False)
        if self.checkXML(".//plot_style//hide_ylabel"):
            self.cluster_map.ax_heatmap.yaxis.set_visible(False)

        return

    def __init__(self, figure, data, plot_XML):
        plot.Plot.__init__(self, figure, data, plot_XML)
        self.cluster_map = 0
        self.vmin = 0
        self.vmax = 100
        self.clusterHierarchy = None
        self.standard_scale = None
        self.z_score = None
        os.makedirs("./process/hierarchy/cluster/", exist_ok=True)
        self.outputHierarchy = glob.glob("./process/hierarchy/cluster/")

        self.data[0].get().set_index("GeneName", inplace=True)

    def initAnimate(self, i):
        return
