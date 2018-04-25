import sys, os
import xml.etree.ElementTree as et
import logging

sys.path.insert(0, "/home/murch/projects/hermes")
sys.path.insert(3, "/home/murch/projects/apollo")
sys.path.insert(2, "/home/murch/projects/athena")
sys.path.insert(1, "/home/murch/projects/factory_managerPY")

import cmd_interface as cmd_interface
import data_manager as dm
import view
import io_util.xml_parse as xml_parser

logger = logging.getLogger(__name__)

def forge(**kwargs):

    data = dm.DataCollection()

    view_collection = view.ViewCollection()

    input = kwargs.get("input")

    if kwargs.get("output"):
        view_collection.set_output_dir(kwargs.get("output"))

    if input is None:
        input = "stdin"

    if len(input) == 1:
        input = input[0]

    data.load_data(input)

    data_dict = data.get_data_dict()

    if kwargs.get("display_xml"):
        display_xml = et.parse(kwargs.get("display_xml"))
        display_dict = xml_parser.xml_to_dict(display_xml.find("display"))
        logger.debug("Global display settings: " + str(display_dict))
    else:
        display_dict = None

    if kwargs.get("style"):
        view_collection.set_global_style(kwargs.get("style"))

    if kwargs.get("plot_xml"):
        view_collection.build_view_sets(et.parse(kwargs.get("plot_xml")), data_dict, display_dict)
    else:
        view_collection.build_view_sets(et.parse(input), data_dict, display_dict)

    view_collection.draw_all_views()

    if kwargs.get("hide_output_flag")==False:
        view_collection.show_all_views()


    if kwargs.get("save_flag")==True:
        view_collection.save_all_views()

    pass

forge_interface = cmd_interface.CmdInterface(forge, os.path.split(__file__)[0] + "/settings_forge.yml")


if __name__ == "__main__":
    forge_interface.run(sys.argv[1:])