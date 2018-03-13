
import io_util.xml_parse as xml_parser
import sys as sys
import factory_manager as fm
import matplotlib.pyplot as plt


import plot_manager as pm
import type as types

import logging
logger = logging.getLogger(__name__)


class View(fm.FactoryObject):
    def initialize(self):
        # self.title = ""
        self.view_style_XML = None
        self.viewset_style_XML = None
        self.figure = None
        self.plot_engine = "matplotlib"
        self.plot_manager = None

    def show(self):
        self.plot_manager.call_all("draw")
        self.plot_manager.call_all("annotate_plot")

    def save(self):
        figure_list = self.plot_manager.get_all("figure")

        for i, fig in enumerate(figure_list):
            fig.savefig("./output/" + self.get("title") + "_" + '{:d}'.format(i) + ".png", bbox_inches="tight",
                        pad_inches=0, transparent=True)
        pass

    def load_plot_manager(self, data_dict):
        plot_settings = xml_parser.xml_to_dict(self.xml.find("view_settings"))

        logger.debug("Loading view settings")

        self.plot_manager = pm.PlotManager(types, kwargs=plot_settings.get("view_settings"))

        self.plot_manager.set("title", self.xml.findtext("title"))

        self.plot_manager.setup_figure()

        self.plot_manager.populate_from_xml(self.xml.iterfind("./plot/subplot"), nested_type="./subplot_settings/plot_type")
        self.plot_manager.call_all("build")

        self.plot_manager.push_all("grid_spec", self.plot_manager.get("grid_spec"))
        self.plot_manager.push_all("figure", self.plot_manager.get("figure"))
        self.plot_manager.call_all("setup_subplot")
        self.plot_manager.call_all("initialize_annotation")
        self.plot_manager.call_all("set_data", data_dict)

        pass


class ViewSet(fm.FactoryStack):
    def initialize(self):
        self.title = None
        self.viewset_XML = None
        self.viewset_style_XML = None

    def show_views(self):
        self.call_all("show")

    def save_views(self):
        self.call_all("save")


class ViewCollection():
    def __init__(self):

        self.view_set_list = []

        pass

    def build_view_sets(self, xml, data_dict):

        logger.debug("Building view sets")
        for view_set in xml.iterfind("viewset"):
            view_set_settings = view_set.find("view_set_style")
            view_set_settings = xml_parser.xml_to_dict(view_set_settings)
            view_set_new = ViewSet(None, kwargs=view_set_settings, xml=view_set)
            view_set_new.set("title", view_set.findtext("title"))
            view_set_new.set_available_class_types({"view": View})

            self.view_set_list.append(view_set_new)

        logger.debug("Views sets loaded from XML: " + str(len(self.view_set_list)))

        for view_set in self.view_set_list:
            view_set.populate_from_xml(view_set.get("xml").iterfind("view"))
            view_set.call_all("load_plot_manager", data_dict)
        pass

    def show_all_views(self):

        for view_set in self.view_set_list:
            view_set.show_views()
            #view_set.save_views()
        plt.show()
