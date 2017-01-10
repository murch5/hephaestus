import contourMap as ctrmap
import generateFrameSet
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as anim

class contourMapAnim():

    def __init__(self, frames):
        self.contourMapBase = ctrmap.contourMap(frames[0])
        self.frames = frames
        self.fig = plt.figure()
        self.subplot = self.fig.add_subplot()
        return;

    def animateContour(n):
        print("test")
        return;

    def animateInit(self):
        print("LOG:    Initialize animation")
        return;

    def startAnim(self):
        print("LOG:    Start animation")
        anim.FuncAnimation(self.fig, self.animateContour(),frames = 10, init_func=self.animateInit())
        plt.show()
        return;

test = generateFrameSet.generateFrameSet("*.tif")

animation = contourMapAnim(test)

animation.startAnim()

#sys.stdout = open('log.txt', 'w')

#sys.stdout.close()
