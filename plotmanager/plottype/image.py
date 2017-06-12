import matplotlib.colors as col
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

from plotmanager.plottype import anim_plot


class Image(anim_plot.AnimPlot):

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

        if self.get("hide_grid"):
            print("booya")
            self.subplot.grid(None, which="both")

        self.image = self.subplot.imshow(self.data[0],cmap=plt.get_cmap(self.color_map),norm=self.normalize)

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
