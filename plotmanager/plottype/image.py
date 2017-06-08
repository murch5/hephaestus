import matplotlib.colors as col
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

from plotmanager.plottype import anim_plot


class Image(anim_plot.AnimPlot):

    def __init__(self,figure, data, plot_settings):
        anim_plot.AnimPlot.__init__(self, figure, data, plot_settings)

        self.type = "image"

        self.image = None
        self.color_bar = None
        self.color_bar_ax = None

        self.normalize = None

        self.init_func_list = {"normalize_luminance": self.normalize_luminance}

        return

    def normalize_luminance(self,settings):

        return


    def add_color_bar(self,image):

        divider = make_axes_locatable(self.subplot)
        self.color_bar_ax = divider.append_axes("right", size="3%", pad=0.05)
        self.color_bar = plt.colorbar(image, cax=self.color_bar_ax, cmap=plt.get_cmap(self.color_map))
        self.color_bar_ax.yaxis.tick_right()
        self.color_bar_ax.xaxis.set_visible(False)

        return

    def clear_color_bar(self):
        if(self.color_bar_ax!=0):
            self.color_bar_ax.remove()

        return

    def draw(self):
        self.subplot.clear()

        if self.get_set_param("hide_grid"):
            print("booya")

            self.subplot.grid(None, which="both")

        self.image = self.subplot.imshow(self.data.get(),cmap=plt.get_cmap(self.get_set_param("color_map")),norm=self.normalize)

       # if self.checkXML(".//plot_style/xlim"):
       #     self.subplot.sex_xlim=(self.getXMLvalue(".//plot_style/xlim"))
       # if self.checkXML(".//plot_style/ylim"):
       #     self.subplot.sex_xlim = (self.getXMLvalue(".//plot_style/ylim"))

      #  if self.checkXML(".//plot_style/color_bar"):
          #  self.clear_color_bar()
           # self.add_color_bar(self.image)

        return

    def getImage(self):
        return self.image
