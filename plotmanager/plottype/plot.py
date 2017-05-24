import matplotlib.gridspec as gridspec
import numpy as np
import pandas as pd

from plotmanager import annotation

class Plot():

    def __init__(self,figure, data, plot_XML):
        self.figure = figure
        self.data = data

        #create data name dict for reference

        self.data_index_dict = {}
        self.set_data_dict()

        self.gridspec = None
        self.subplot = None

        self.plot_XML = plot_XML

        return

    def set_data_dict(self):

        for i,datum in enumerate(self.data):
            self.data_index_dict.update({datum.get_name(): i})

    def set_gridspec(self,gridspec):
        self.gridspec = gridspec

    def animate(self,i):

        return

    def initAnimate(self, i):
        return

    def draw(self):
        return

    def init(self):
        return

    def setup_subplot(self):

        row = int(self.plot_XML.findtext(".//pos/row"))
        col = int(self.plot_XML.findtext(".//pos/col"))
        row_width = int(self.plot_XML.findtext(".//rowsize"))
        col_width = int(self.plot_XML.findtext(".//colsize"))

        subplotspec = self.gridspec.new_subplotspec([row,col], row_width, col_width)

        if self.figure is not None:
            self.subplot = self.figure.add_subplot(subplotspec)

        return

    def checkXML(self,xml):
        check = False
        if self.plot_XML.find(xml) is not None:
            check = True
        else:
            check = False

        return check

    def getXMLvalue(self,xml):
        data = self.plot_XML.find(xml)
        data_type = data.attrib["data_type"]
        value = None
        if data_type in ["int","i"]:
            value = int(data.text)
        elif data_type in ["float","f"]:
            value = float(data.text)
        elif data_type in ["bool","b"]:
            value = bool(data.text)
        elif data_type in ["str","s"]:
            value = str(data.text)
        elif data_type in ["tuple_int", "ti"]:
            value = tuple(data.text.split(","))
        else:
            value = str(data.text)

        return value




