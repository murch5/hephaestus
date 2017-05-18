import plot_class.contourMap as ctrmap
import generateFrameSet
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import numpy as np
import scipy.interpolate
from plot_class.contourMap import contourMap

class contourMapAnim(contourMap):

    def __init__(self, figure, data, position,title="",plotArgs=[],annotate=[]):
        contourMap.__init__(self,figure,data,position,title,plotArgs,annotate)
        self.frames = data
        self.position = position
        self.currFrame = data[0]
        self.fig = figure
        self.animHandler = []
        self.framesPerImage = 1
        self.currFrameIndex = 0
        self.currImageIndex = 0

        print(self.fig)
        print(self.subplot)
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
