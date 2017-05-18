import matplotlib.pyplot as plt

from plot_class import image


class imageStack(image.image):

    def __init__(self,figure, data, position, title="",plotArgs=[],annotate=[]):
        image.image.__init__(self, figure, data, position, title, plotArgs, annotate)
        self.frames = data
        self.currFrame = data[0]
        self.framesPerImage = 1
        self.currFrameIndex = 0
        self.currImageIndex = 0


        return;

    def animate(self, i):

        self.currFrameIndex += 1

        if self.currFrameIndex == self.framesPerImage:
            self.currFrameIndex = 0
            self.currImageIndex += 1

        if self.currImageIndex == len(self.frames) - 1:
            self.currFrameIndex = 0
            self.currImageIndex = 0

        self.currFrame = self.frames[i]

        self.subplot.clear()

        self.draw()

        return;

    def draw(self):
        self.subplot.clear()

        self.image = self.subplot.imshow(self.currFrame.T,cmap=plt.get_cmap(self.colorMap),norm=self.normalize)

        if self.retrieveArgVal("colorBar") is not None:
            self.clearColorBar()
            self.addColorBar(self.image)

        if self.insetLabel == True:
            self.subplot.annotate(self.plotTitle, xy=(1, 0), xycoords='axes fraction',
                                  xytext=(0.85, 0.1), textcoords='axes fraction', color="white", weight="semibold", size="medium")


        return;
