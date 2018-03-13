import sys, os
import xml.etree.ElementTree as et

sys.path.insert(0, "/home/murch/projects/hermes")
sys.path.insert(3, "/home/murch/projects/apollo")
sys.path.insert(2, "/home/murch/projects/athena")
sys.path.insert(1, "/home/murch/projects/factory_managerPY")

import cmd_interface as cmd_interface
import data_manager as dm
import view


def forge(**kwargs):

    data = dm.DataCollection()

    view_collection = view.ViewCollection()

    input = kwargs.get("input")
    print(input)
    if input is None:
        input = "stdin"

    if len(input)==1:
        input = input[0]

    data.load_data(input)

    data_dict = data.get_data_dict()

    print(input)

    if kwargs.get("plot_xml"):
        view_collection.build_view_sets(et.parse(kwargs.get("plot_xml")), data_dict)
    else:
        view_collection.build_view_sets(et.parse(input), data_dict)

    view_collection.show_all_views()

    pass


forge_interface = cmd_interface.CmdInterface(forge, os.path.split(__file__)[0] + "/settings_forge.yml")


if __name__ == "__main__":
    forge_interface.run(sys.argv[1:])