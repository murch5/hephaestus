import yaml as yaml
import io as io
import io_util.xml_parse as xml_parser

import factory_manager as fm
import data_manager as dm
import annotation_manager as am
import anno as am_class

import os as os

import logging
logger = logging.getLogger(__name__)

class Plot(fm.FactoryObject):

    def initialize(self):
        self.load_plot_settings()
        self.annotation_manager = None

        pass

    def draw(self):
        return

    def annotate_plot(self):

        logging.debug("--- Adding annotations")

        self.annotation_manager.call_all("draw")

        pass

    def build(self):

        logger.debug("Build plot")

        self.update_attr(self.plot_style)

        annotate_XML = self.xml.find("annotate")

        plot_style_settings = self.xml.find("plot_style")



        self.update_attr(xml_parser.xml_to_dict(plot_style_settings))

        self.annotation_manager = am.AnnotationManager(am_class)

        self.annotation_manager.populate_from_xml(annotate_XML)

        pass

    def setup_subplot(self):

        self.update_attr(self.subplot_settings)
        row = int(self.row)
        col = int(self.col)
        row_width = int(self.row_size)
        col_width = int(self.col_size)

        subplotspec = self.grid_spec.new_subplotspec([row,col], row_width, col_width)

        if self.figure is not None:
            self.subplot = self.figure.add_subplot(subplotspec)
        else:
            self.subplot = None

        return

    def set_data(self, data_dict):

        data_list = []

        self.data = [data_dict.get(self.xml.findtext("source"))]

        pass

    def load_plot_settings(self):

        with io.open(os.path.split(__file__)[0] + "/" + self.subplot_settings.get("plot_type") + ".yml","r") as plot_config:
            try:
                self.type_settings = yaml.safe_load(plot_config)
            except:
                logger.error("Plot type config " + self.plot_type + ".yml failed to load")

        logger.debug(self.type_settings)
        self.update_attr(self.type_settings, overlap="drop")

        return

    def initialize_annotation(self):
        self.annotation_manager.push_all("ax",self.subplot)
