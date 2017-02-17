import animPlot
import matplotlib.pyplot as plt
import matplotlib.colors as col
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np

class image(animPlot.animPlot):

    def __init__(self,figure, data, position, title="",plotArgs=[]):
        animPlot.animPlot.__init__(self,figure, data, position,title,plotArgs)
        self.data = data
        self.colorMap = self.retrieveArgVal("cmap")
        self.colorBar = 0
        self.colorBarAx = 0
        self.luminMin = None
        self.luminMax = None
        self.normalize = self.normalizeLumin()

        self.image = 0
        return;

    def normalizeLumin(self):

        if self.retrieveArgVal("luminMin") is not None:
            self.luminMin = int(self.retrieveArgVal("luminMin"))

        if self.retrieveArgVal("luminMax") is not None:
            self.luminMax = int(self.retrieveArgVal("luminMax"))

        normalize = col.Normalize(self.luminMin,self.luminMax)

        return normalize

    def animate(self, i):

        self.draw()

        return;

    def addColorBar(self,image):

        divider = make_axes_locatable(self.subplot)
        self.colorBarAx = divider.append_axes("right", size="3%", pad=0.05)
        self.colorBar = plt.colorbar(image, cax=self.colorBarAx, cmap=plt.get_cmap(self.colorMap))
        self.colorBarAx.yaxis.tick_right()
        self.colorBarAx.xaxis.set_visible(False)

        return
    def clearColorBar(self):
        if(self.colorBarAx!=0):
            self.colorBarAx.remove()

        return

    def draw(self):
        self.subplot.clear()


        print(self.data)
        self.image = self.subplot.imshow(self.data.T,cmap=plt.get_cmap(self.colorMap),norm=self.normalize)

        if len(self.xlim) > 0:
            self.subplot.set_xlim(self.xlim)
        if len(self.ylim) > 0:
            self.subplot.set_ylim(self.ylim)

        if self.retrieveArgVal("colorBar") is not None:
            self.clearColorBar()
            self.addColorBar(self.image)

        if self.insetLabel == True:
            self.subplot.annotate(self.plotTitle, xy=(1, 0), xycoords='axes fraction',
                                  xytext=(0.85, 0.1), textcoords='axes fraction', color="white", weight="semibold", size="medium")

        return

    def getImage(self):
        return self.image
