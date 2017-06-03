import matplotlib.gridspec as gridspec
import numpy as np
import pandas as pd
import yaml as yaml
import io as io

import os as os

import logging
logger = logging.getLogger(__name__)

from plotmanager import annotation

class Plot():

    def __init__(self,figure, data, plot_XML):
        self.figure = figure
        self.data = data

        self.type = None
        self.type_settings = None

        self.plot_settings = {}
        self.toggle_settings = {}
        self.init_func = {}

        self.param_list = []

        self.gridspec = None
        self.subplot = None

        self.plot_XML = plot_XML

        return

    def set_gridspec(self,gridspec):
        self.gridspec = gridspec

    def render(self):
        return

    def draw(self):

        self.render()

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

    def getXMLvalue(self,xml,xml_subset=None):

        if xml_subset is not None:
            data = xml_subset.find(xml)
        else:
            data = self.plot_XML.find(xml)

        if data is not None:
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
        else:
            value = None

        return value

    def getXMLsubset(self,xml,xml_set=None):

        subset = None
        if xml_set is not None:
            subset = xml_set.find(xml)
        else:
            subset = self.plot_XML.find(xml)

        return subset

    def initialize(self):

        logger.info("--- Initializing plot...")

        self.parse_xml()
        self.load_plot_settings()
        self.set_parameters()
        self.toggle_parameters()
        self.initialize_func()

        return

    def parse_xml(self):
        return

    def set_parameters(self):
        return

    def toggle_parameters(self):
        return

    def initialize_func(self):

        return

    def get_set_param(self,name):
        return self.plot_settings.get(name)

    def load_plot_settings(self):

        with io.open(os.path.split(__file__)[0] + "/" + self.type + ".yml","r") as plot_config:
            try:
                self.type_settings = yaml.safe_load(plot_config)
            except:
                logger.error("Plot type config " + self.type + ".yml failed to load")

        print(self.type_settings)

        self.plot_settings = self.type_settings.get("set_parameters")
        logger.debug("--- Plot settable parameters: " + str(self.plot_settings))

        self.toggle_settings = self.type_settings.get("toggle_parameters")
        logger.debug("--- Plot toggle parameters: " + str(self.toggle_settings))

        self.init_func = self.type_settings.get("init_func")
        logger.debug("--- Plot initialization functions: " + str(self.init_func))

        return




