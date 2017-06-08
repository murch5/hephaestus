import matplotlib.gridspec as gridspec
import numpy as np
import pandas as pd
import yaml as yaml
import io as io

import io_util.xml_parse as xml_parser



import os as os

import logging
logger = logging.getLogger(__name__)


from plotmanager import annotation

class Plot():

    def __init__(self,figure, data, plot_settings):
        self.figure = figure
        self.data = data

        self.type = None
        self.type_settings = None

        self.set_params = {}
        self.toggle_settings = {}
        self.init_func_settings = {}

        self.init_func_list = {}
        self.toggle_func_list = {"axes":self.set_axes}

        self.param_list = []

        self.gridspec = None
        self.subplot = None

        self.plot_settings = plot_settings.get("subplot")
        self.plot_style = self.plot_settings.get("plot_style")

        logger.debug("--- Plot settings: " + str(self.plot_settings))

        return

    def set_gridspec(self,gridspec):
        self.gridspec = gridspec

    def render(self):
        return

    def draw(self):

        self.render()

        return

    def compile_init_func_list(self):

        return

    def setup_subplot(self):

        row = int(self.plot_settings.get("pos").get("row"))
        col = int(self.plot_settings.get("pos").get("col"))
        row_width = int(self.plot_settings.get("rowsize"))
        col_width = int(self.plot_settings.get("colsize"))

        subplotspec = self.gridspec.new_subplotspec([row,col], row_width, col_width)

        if self.figure is not None:
            self.subplot = self.figure.add_subplot(subplotspec)

        return

    def initialize(self):

        logger.info("--- Initializing plot...")

        self.load_plot_settings()
        self.set_parameters()
        self.toggle_parameters()
        self.initialize_func()

        return

    def set_parameters(self):

        for param in self.plot_style:
            if param in self.set_params:
                self.set_params[param] = self.plot_style.get(param)
            if param in self.toggle_settings:
                self.toggle_settings[param] = self.plot_style.get(param)
            if param in self.init_func:
                self.init_func[param] = self.plot_style.get(param)
        return

    def toggle_parameters(self):


        for toggle in self.toggle_settings.keys():
            if self.toggle_settings[toggle]:
                self.get_toggle_func_list().get(toggle)(self.toggle_settings[toggle])

        return

    def initialize_func(self):

        for func in self.init_func.keys():
            if self.init_func[func]:
                self.get_init_func_list().get(func)(self.init_func[func])

        return

    def get_set_param(self,name):
        return self.set_params.get(name)

    def load_plot_settings(self):

        with io.open(os.path.split(__file__)[0] + "/" + self.type + ".yml","r") as plot_config:
            try:
                self.type_settings = yaml.safe_load(plot_config)
            except:
                logger.error("Plot type config " + self.type + ".yml failed to load")

        self.set_params = self.type_settings.get("set_parameters")
        logger.debug("--- Plot settable parameters: " + str(self.plot_settings))

        self.toggle_settings = self.type_settings.get("toggle_parameters")
        logger.debug("--- Plot toggle parameters: " + str(self.toggle_settings))

        self.init_func = self.type_settings.get("init_func")
        logger.debug("--- Plot initialization functions: " + str(self.init_func))

        return

    def get_init_func_list(self):
        return self.init_func_list

    def get_toggle_func_list(self):
        return self.toggle_func_list

    ##Toggle Functions Declarations

    def set_axes(self,settings):

        if settings.get("grid"):
            axis = None
            show = True

            x_grid = settings.get("grid").get("x")
            y_grid = settings.get("grid").get("y")

            if x_grid == True:
                axis = "x"
            if y_grid == True:
                axis = "y"
            if x_grid == True and y_grid == True:
                axis = "both"

            if axis is None:
                show = False
                axis = "both"

            self.subplot.axes.grid(b=show,axis=axis)


        pass

    def title(self,settings):
        pass

    def axes_labels(self,settings):
        pass

