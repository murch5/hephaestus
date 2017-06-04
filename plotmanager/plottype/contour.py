import numpy as np


from plotmanager.plottype import image


class ContourMap(image.Image):

    def initContourMap(self):

        dim = self.surfaceData.shape

        self.x = np.arange(0, dim[0])
        self.y = np.arange(0, dim[1])
        self.addLinesFlag = False
        self.lineDrawFunc = None
        self.meshX, self.meshY = np.meshgrid(self.x, self.y)

        return

    def __init__(self,figure, data, plot_settings):
        image.Image.__init__(self,figure, data, plot_settings)
        self.surfaceData = data[0]
        self.currFrame = data[0]
        self.x = []
        self.y = []
        self.meshX = []
        self.meshY = []
        self.contourPlot = []

        self.subplot.axis("equal")

        self.initContourMap()

        return

    def draw(self):
       # print("LOG:    Draw initial step of contour map")
        self.subplot.cla()
        levels =[11,17,20,40,80]
        self.contourPlot = self.subplot.contour(self.meshX, self.meshY, self.surfaceData.T, zdir='z',linewidths=1,cmap="viridis", levels=levels)
        self.image = self.contourPlot
        if self.addLinesFlag == True:
            self.lineDrawFunc()

        if self.checkXML(".//plot_style/colorbar"):
            self.clear_color_bar()
            self.add_color_bar(self.contourPlot)

        self.color_bar.outline.set_linewidth(0.2)
        for line in self.color_bar.lines:
            line.set_linewidth(5.0)

        if self.checkXML(".//plot_style/xlim"):
            self.subplot.set_xlim(self.getXMLvalue(".//plot_style/xlim"))
        if self.checkXML(".//plot_style/ylim"):
            self.subplot.set_ylim(self.getXMLvalue(".//plot_style/xlim"))

        self.subplot.invert_yaxis()

        return

    def setSurfaceData(self, data):
        self.surfaceData = data.T
        return

    def assignLineDrawFunc(self,lineFunc):

        self.addLinesFlag = True
        self.lineDrawFunc = lineFunc

        return;

    def animate(self,i):
        self.currFrameIndex += 1


        if self.currFrameIndex == self.framesPerImage:
            self.currFrameIndex = 0
            self.currImageIndex += 1

        if self.currImageIndex == len(self.frames) - 1:
            self.currFrameIndex = 0
            self.currImageIndex = 0

        it = np.nditer(self.currFrame, flags=['multi_index'])
        while not it.finished:
            self.currFrame[it.multi_index] = self.frames[self.currImageIndex][it.multi_index] + ((self.frames[(
            self.currImageIndex + 1)][it.multi_index] - self.frames[self.currImageIndex][it.multi_index]) * (
                                                                                                 self.currFrameIndex / 20))

            it.iternext()

        self.surfaceData = self.currFrame
        self.subplot.clear()

        self.draw()

        return self.subplot

    def initAnimate(self, i):
        self.draw()
        return;