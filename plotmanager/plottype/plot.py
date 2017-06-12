
import yaml as yaml
import io as io

import factory_manager as fm



import os as os

import logging
logger = logging.getLogger(__name__)


from plotmanager import annotation

class Plot(fm.FactoryObject):


    def initialize(self):
        self.load_plot_settings()
        pass

    def set_gridspec(self,gridspec):
        self.gridspec = gridspec

    def render(self):
        return

    def draw(self):

        self.render()

        return

    def do(self, data):
        self.draw()
        pass


    def compile_init_func_list(self):

        return

    def setup_subplot(self):

        row = int(self.row)
        col = int(self.col)
        row_width = int(self.row_size)
        col_width = int(self.col_size)

        subplotspec = self.grid_spec.new_subplotspec([row,col], row_width, col_width)

        if self.figure is not None:
            self.subplot = self.figure.add_subplot(subplotspec)

        return

    def set_data(self):
        self.data = self.data_manager.get_all("data")
        pass

    def load_plot_settings(self):

        with io.open(os.path.split(__file__)[0] + "/" + self.plot_type + ".yml","r") as plot_config:
            try:
                self.type_settings = yaml.safe_load(plot_config)
            except:
                logger.error("Plot type config " + self.plot_type + ".yml failed to load")

        self.update_attr(self.type_settings,overlap="drop")

        return


