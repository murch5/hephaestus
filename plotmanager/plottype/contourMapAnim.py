import matplotlib.animation as anim
import matplotlib.pyplot as plt
import numpy as np

from plotmanager.plottype import contourMap


class ContourMapAnim(contourMap.ContourMap):

    def __init__(self,figure, data, plot_XML):
        contourMap.ContourMap.__init__(self,figure, data, plot_XML)
        self.frames = data
        self.currFrame = data[0]
        self.fig = figure
        self.animHandler = []
        self.framesPerImage = 1
        self.currFrameIndex = 0
        self.currImageIndex = 0

        return;

    def animateContour(self,i):
        self.currFrameIndex += 1

        if self.currFrameIndex == self.framesPerImage:
            self.currFrameIndex = 0
            self.currImageIndex += 1

        if self.currImageIndex == len(self.frames)-1:
            self.currFrameIndex = 0
            self.currImageIndex = 0

        it = np.nditer(self.currFrame, flags=['multi_index'])
        while not it.finished:

            self.currFrame[it.multi_index] = self.frames[self.currImageIndex][it.multi_index] + ((self.frames[(self.currImageIndex+1)][it.multi_index]- self.frames[self.currImageIndex][it.multi_index])*(self.currFrameIndex/20))

            it.iternext()

        self.surfaceData = self.currFrame
        self.subplot.clear()
        contourMap.draw(self)
        return self.subplot

    def animateInit(self):
        print("LOG:    Initialize animation")
        contourMap.draw(self)
        return self.subplot

    def startAnim(self):
        print("LOG:    Start animation")
        self.animHandler = anim.FuncAnimation(self.fig, self.animateContour,frames = self.framesPerImage*len(self.frames), init_func=self.animateInit)
        plt.show()
        return


#sys.stdout = open('log.txt', 'w')

#sys.stdout.close()
