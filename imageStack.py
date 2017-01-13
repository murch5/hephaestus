import animPlot as animPlot
import matplotlib.pyplot as plt

class imageStack(animPlot.animPlot):

    def __init__(self,figure, data, position, dataDir):
        animPlot.animPlot.__init__(self,figure, data, position)
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

        self.subplot.imshow(self.currFrame.T)
        self.subplot.invert_yaxis()

        return;

    def draw(self):
        self.subplot.clear()
        self.subplot.imshow(self.currFrame.T)
        return;
