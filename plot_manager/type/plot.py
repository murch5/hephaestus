
import yaml as yaml
import io as io

import factory_manager as fm



import os as os

import logging
logger = logging.getLogger(__name__)

class Plot(fm.FactoryObject):

    def initialize(self):
        self.load_plot_settings()
        pass

    def draw(self):
        return

    def annotate(self):

        logging.debug("--- Adding annotations")

        self.annotation_manager.call_all("draw")

        pass

    def setup_subplot(self):

        row = int(self.row)
        col = int(self.col)
        row_width = int(self.row_size)
        col_width = int(self.col_size)

        subplotspec = self.grid_spec.new_subplotspec([row,col], row_width, col_width)

        if self.figure is not None:
            self.subplot = self.figure.add_subplot(subplotspec)

        #self.annotation

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

        logger.debug(self.type_settings)
        self.update_attr(self.type_settings,overlap="drop")

        return

    def initialize_annotation(self):
        self.annotation_manager.push_all("ax",self.subplot)
