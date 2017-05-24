import matplotlib.colors as col
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

from plotmanager.plottype import animPlot


class Image(animPlot.AnimPlot):

    def __init__(self,figure, data, plot_XML):
        animPlot.AnimPlot.__init__(self,figure, data, plot_XML)
        self.image = 0
        self.color_bar = 0
        self.color_bar_ax = 0
        self.lumin_min = None
        self.lumin_max = None
        self.normalize = self.normalize_lumin()

        self.color_map = "Greys"

        return

    def normalize_lumin(self):

        if self.checkXML(".//plot_style/lumin"):
            self.lumin_min = self.getXMLvalue(".//plot_style/lumin/min")
            self.lumin_max = self.getXMLvalue(".//plot_style/lumin/max")

        normalize = col.Normalize(self.lumin_min,self.lumin_max)

        return normalize

    def animate(self, i):

        self.draw()

        return;

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

        self.image = self.subplot.imshow(self.data.get().T,cmap=plt.get_cmap(self.color_map),norm=self.normalize)

        if self.checkXML(".//plot_style/xlim"):
            self.subplot.sex_xlim=(self.getXMLvalue(".//plot_style/xlim"))
        if self.checkXML(".//plot_style/ylim"):
            self.subplot.sex_xlim = (self.getXMLvalue(".//plot_style/ylim"))

        if self.checkXML(".//plot_style/color_bar"):
            self.clear_color_bar()
            self.add_color_bar(self.image)

       # if self.insetLabel == True:
           # self.subplot.annotate(self.plotTitle, xy=(1, 0), xycoords='axes fraction',
             #                     xytext=(0.85, 0.1), textcoords='axes fraction', color="white", weight="semibold", size="medium")

        return

    def getImage(self):
        return self.image
