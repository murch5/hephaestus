import sys

import logging
logger = logging.getLogger(__name__)

import matplotlib.pyplot as plt

import factory_manager as fm
import matplotlib.gridspec as gridspec


plt.rcParams['animation.ffmpeg_path'] = '/ffmpeg/bin/ffmpeg'
plt.rcParams['image.cmap'] = 'magma'


class PlotManager(fm.FactoryStack):

    def setup_figure(self):

        if self.engine == "matplotlib":
            logger.debug("--- Plot manager name: matplotlib")
            self.figure = plt.figure(figsize=(11, 9))
            #self.figure.canvas.set_window_title(self.name)
        else:
            logger.debug("--- Plot manager name: seaborn")
            self.figure = None

        row = self.row
        col = self.col

        self.grid_spec = gridspec.GridSpec(int(row), int(col))


    def on_resize(self, event):
        print("Resizing...")
        self.draw_plots()
        self.figure.canvas.flush_events()
        return

    def initialize(self):
        pass

