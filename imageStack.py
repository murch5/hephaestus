import animPlot as animPlot
import matplotlib.pyploy as plt

class imageStack(animPlot.animPlot):

    def __init__(self,figure, data, position):
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

        self.currFrame = self.frame[i]

        self.subplot.clear()
        self.subplot = plt.imshow(self.currFrame)

        return;

    def draw(self):
        self.subplot.clear()
        self.subplot = plt.imshow(self.currFrame)
        return;
