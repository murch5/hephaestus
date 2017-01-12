import contourMap as ctrmap
import generateFrameSet
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import numpy as np
import scipy.interpolate

class contourMapAnim:

    def __init__(self, data, position):
        self.frames = data
        self.position = position
        self.currFrame = data[0]
        self.fig = plt.figure()
        self.subplot = self.fig.add_subplot(111,aspect='equal')
        self.animHandler = []
        self.contourMapBase = ctrmap.contourMap(self.currFrame, self.subplot)
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

        self.contourMapBase.setSurfaceData(self.currFrame)
        self.subplot.clear()
        self.contourMapBase.drawContour()
        return self.subplot

    def animateInit(self):
        print("LOG:    Initialize animation")
        self.contourMapBase.drawContour()
        return self.subplot

    def startAnim(self):
        print("LOG:    Start animation")
        self.animHandler = anim.FuncAnimation(self.fig, self.animateContour,frames = self.framesPerImage*len(self.frames), init_func=self.animateInit)
        plt.show()
        return

    def


#sys.stdout = open('log.txt', 'w')

#sys.stdout.close()
