import matplotlib.gridspec as gridspec
import numpy as np
import pandas as pd

from plotmanager import annotation

class Plot():

    def __init__(self,figure, data, plot_XML):
        self.figure = figure
        self.data = data
        self.gridspec = None
        self.subplot = None

        self.plot_XML = plot_XML

        return

    def set_gridspec(self,gridspec):
        self.gridspec = gridspec

    def animate(self,i):

        return;

    def initAnimate(self, i):
        return;

    def draw(self):
        return;

    def init(self):
        return;

    def setup_subplot(self):

        row = int(self.plot_XML.findtext(".//pos/row"))
        col = int(self.plot_XML.findtext(".//pos/col"))
        row_width = int(self.plot_XML.findtext(".//rowsize"))
        col_width = int(self.plot_XML.findtext(".//colsize"))

        subplotspec = self.gridspec.new_subplotspec([row,col], row_width, col_width)

        self.subplot = self.figure.add_subplot(subplotspec)

        return




