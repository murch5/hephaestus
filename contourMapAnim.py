import contourMap as ctrmap
import generateFrameSet
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as anim

class contourMapAnim():

    def __init__(self, frames):
        self.frames = frames
        self.fig = plt.figure()
        self.subplot = self.fig.add_subplot(1,1,1)
        self.animHandler = []
        self.contourMapBase = ctrmap.contourMap(frames[0], self.subplot)
        self.framesPerImage = 20
        self.currFrame = 0
        self.currImage = 0

        print(self.fig)
        print(self.subplot)
        return;

    def animateContour(self,i):
        self.currFrame += 1

        if self.currFrame == self.framesPerImage:
            self.currFrame = 0
            self.currImage += 1



        return;

    def animateInit(self):
        print("LOG:    Initialize animation")
        self.contourMapBase.drawContour()
        return;

    def startAnim(self):
        print("LOG:    Start animation")
        self.animHandler = anim.FuncAnimation(self.fig, self.animateContour,frames = self.framesPerImage*len(self.frames), init_func=self.animateInit)
        plt.show()
        return;

test = generateFrameSet.generateFrameSet("*.tif")

animation = contourMapAnim(test)

animation.startAnim()

#sys.stdout = open('log.txt', 'w')

#sys.stdout.close()
