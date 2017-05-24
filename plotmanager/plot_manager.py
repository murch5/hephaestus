import matplotlib.animation as anim
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb
from plotmanager.plottype.DNAtrack import DNAtrack
from plotmanager.plottype.clusterMap import ClusterMap
from plotmanager.plottype.contourMap import ContourMap
from plotmanager.plottype.forest import Forest
from plotmanager.plottype.imageStack import ImageStack
from plotmanager.plottype.pie import Pie
from plotmanager.plottype.proteinTrack import ProteinTrack
from plotmanager.plottype.scatter import Scatter
from plotmanager.plottype.survival import Survival
from plotmanager.plottype.swarmInterval import SwarmInterval
from plotmanager.plottype.track import Track
from plotmanager.plottype.variantTrack import VariantTrack
from plotmanager.plottype.venn import Venn
from plotmanager.plottype.violin import Violin
from plotmanager.plottype.zb_peristalsis import ZbPeristalsis

from plotmanager.plottype.image import Image

import matplotlib.gridspec as gridspec
import datatypes as dt


plt.rcParams['animation.ffmpeg_path'] = '/ffmpeg/bin/ffmpeg'
plt.rcParams['image.cmap'] = 'magma'

chartTypes = {"violin": Violin, "pie": Pie, "scatter": Scatter, "forest": Forest, "contour": ContourMap,
              "imageStack": ImageStack, "zbperistalsis": ZbPeristalsis, "image": Image, "swarmInterval": SwarmInterval,
              "survival": Survival, "track": Track, "proteinTrack": ProteinTrack, "DNAtrack": DNAtrack,
              "variantTrack": VariantTrack, "clusterMap": ClusterMap, "venn": Venn}

class plot_manager():
    def __init__(self, name, viewset_style,view):
        self.name = name

        self.viewset_XML_style = viewset_style
        self.view_XML = view

        if str(self.view_XML.findtext(".//plot_engine")) == "matplotlib":
            self.figure = plt.figure(figsize=(11, 9))
        else:
            self.figure = None

        self.plot_list = []
        self.grid_spec = None

        self.setup_figure()


        return

    def setup_figure(self):

        row = self.view_XML.find(".//plotsize/row").text
        col = self.view_XML.find(".//plotsize/col").text

        self.grid_spec = gridspec.GridSpec(int(row), int(col))


    def onResize(self, event):
        print("Resizing...")
        self.draw_plots()
        self.figure.canvas.flush_events()
        return

    def add_plot(self,data,type,plot_XML):

        new_plot = chartTypes[type](self.figure,data,plot_XML)
        new_plot.set_gridspec(self.grid_spec)
        new_plot.setup_subplot()

        self.plot_list.append(new_plot)


    def get_figure(self):
        return self.figure

    def draw_plots(self):

        for plot in self.plot_list:
            plot.draw()

        return

    def show_plots(self):
        plt.show()

    def set_gridspec(self,gridspec):
        self.gridspec = gridspec


