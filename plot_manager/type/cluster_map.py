from type import plot
import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd

import logging as logging
logger = logging.getLogger(__name__)


import numpy as np
import glob as glob
import os as os

import scipy.spatial.distance as sp_spatial_distance
import scipy.cluster.hierarchy as sp_cluster_hierarchy

import sys

sys.setrecursionlimit(40000)

class ClusterMap(plot.Plot):

    def hierarchical_clustering(self, settings):

        os.makedirs("./process/hierarchy/cluster/", exist_ok=True)
        self.output_hierarchy = glob.glob("./process/hierarchy/cluster/")

        logger.debug("------ Hierarchical clustering enabled")

        if settings.get("source") == "save":

            data_transpose = self.data.get().T
            pairwise_dist = sp_spatial_distance.pdist(data_transpose)
            self.clusterHierarchy = sp_cluster_hierarchy.linkage(pairwise_dist, method="complete")
            clusterNameOutput = str(settings.get("name")) + ".cluster"

            logger.debug("--------- Save hierarchy as:" + str(clusterNameOutput))

            clusterOutputPath = os.path.join("./process/hierarchy/cluster/", clusterNameOutput)
            self.clusterHierarchy.dump(clusterOutputPath)

        elif settings.get("source") == "get":

            clusterinput_name = str(str(settings.get("name"))) + ".cluster"
            clusterinput_path = os.path.join("./process/hierarchy/cluster/", clusterinput_name)
            self.clusterHierarchy = np.load(clusterinput_path)

        return

    def group_by(self, settings):

        if self.init_func.get("groupby_color") is not None:

            subset = self.getXMLsubset(".//plot_style//groupby_color")

            for set in subset.findall(".//grouping"):
                axis = self.getXMLvalue(".//axis", set)

                groups_color_mapping = self.getXMLvalue(".//colormap_name", set)

                mapping_subset = self.getXMLsubset(".//name_mapping", set)

                name_transforms = mapping_subset.findall(".//mapping")

                index_names = pd.Series(self.data.get_data_obj().get_index_labels(axis))

                groups_name = index_names

                for maps in name_transforms:
                    dataset_map = self.getXMLvalue(".//name", maps)

                    groups_name = self.data.map_transform(groups_name, self.data.get_byname(dataset_map))

                if self.getXMLvalue(".//color_map", set):
                    group_color_palette = sb.color_palette(self.getXMLvalue(".//color_map", set), len(groups_name))
                    group_color_pal_dict = dict(zip(groups_name, group_color_palette))

                    ### Override nan to white
                    group_color_pal_dict[np.nan] = (1.0, 1.0, 1.0)

                    group_color = self.data.map_transform(groups_name, group_color_pal_dict)
                else:
                    group_color = self.data.map_transform(groups_name, self.data.get_byname(groups_color_mapping))

                groups_indexed = pd.concat([index_names, group_color], ignore_index=False, axis=1)
                groups_indexed.columns = ["Indices", "Classification", ]
                groups_indexed.set_index("Indices", inplace=True)

                if axis == 1:
                    self.col_color_groups = groups_indexed
                elif axis == 0:
                    self.row_color_groups = groups_indexed

        return

    def draw(self):

        self.data[0].set_index("GeneName", inplace=True)
        self.cluster_map = sb.clustermap(self.data[0], col_linkage=self.cluster_hierarchy, vmin=self.vmin, row_linkage=None,
                                         vmax=self.vmax, standard_scale=self.std_scale, z_score=self.z_score,col_colors=self.col_color_groups,
                                         row_colors = self.row_color_groups, figsize=(15, 8))

        plt.setp(self.cluster_map.ax_heatmap.get_yticklabels(), rotation=0)
        plt.setp(self.cluster_map.ax_heatmap.get_xticklabels(), rotation=90)

        self.figure = self.cluster_map.fig


        return


        #


