
import io_util.xml_parse as xml_parser
import sys as sys
import factory_manager as fm
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sb

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

    def draw_plots(self):
        self.plot_manager.call_all("draw")
        self.plot_manager.call_all("annotate_plot")

    def save(self):
        figure_list = self.plot_manager.get_all("figure")

        self.dpi = 600

        for i, fig in enumerate(figure_list):
            fig.savefig(self.output_dir + self.get("title") + "_v" + '{:d}'.format(i) + ".png", bbox_inches="tight",
                        pad_inches=0, transparent=False, dpi=self.dpi)
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
        self.output_dir = None

    def draw_views(self):
        self.call_all("draw_plots")

    def save_views(self):
        self.push_all("output_dir",self.output_dir)
        self.call_all("save")

class ViewCollection():
    def __init__(self):

        self.view_set_list = []
        self.output_dir = "./output/"
        self.display_dict = None
        pass

    def build_view_sets(self, xml, data_dict, display_dict=None):

        logger.debug("Building view sets")
        for view_set in xml.iterfind("viewset"):
            view_set_settings = view_set.find("view_set_style")
            view_set_settings = xml_parser.xml_to_dict(view_set_settings)
            view_set_new = ViewSet(None, kwargs=view_set_settings, xml=view_set)
            view_set_new.set("title", view_set.findtext("title"))
            view_set_new.set("output_dir", self.output_dir)
            view_set_new.set_available_class_types({"view": View})

            if display_dict:
                self.display_dict = display_dict
                view_set_new.push_all_attr_dict(display_dict.get("display"), overlap="overwrite")
                self.set_global_style_params()
                print("booya")
            self.view_set_list.append(view_set_new)

        logger.debug("Views sets loaded from XML: " + str(len(self.view_set_list)))

        for view_set in self.view_set_list:
            view_set.populate_from_xml(view_set.get("xml").iterfind("view"))
            view_set.call_all("load_plot_manager", data_dict)
        pass

    def draw_all_views(self):

        for view_set in self.view_set_list:
            view_set.draw_views()

    def show_views(self):
        plt.show()
        pass


    def save_all_views(self):
        for view_set in self.view_set_list:
            view_set.save_views()
        pass

    def set_output_dir(self, out):
        self.output_dir = out
        pass

    def set_global_style_params(self):

        if self.display_dict:
            #plt.rc(**self.global_style_dict)
            ##font.size
            pass

        pass

    def set_global_style(self, style_sheet_path):
        logger.debug("Global style sheet path: " + str(style_sheet_path))
        plt.style.use(style_sheet_path)

        style_rc = mpl.rc_params_from_file(style_sheet_path)
        #sb.set(rc=style_rc)
        #sb.set(font="Helvetica")
        #sb.set_style("white")
        #sb.set(font_scale = 2)
        plt.rcParams['font.sans-serif'] = ["Helvetica", "sans-serif"]
        pass