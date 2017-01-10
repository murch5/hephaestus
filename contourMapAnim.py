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
        return;

    def animateInit(self):
        return;

    def startAnim(self):

        anim.FuncAnimation(self.fig, self.animateContour(),frames = 2, init_func=self.animateInit(), interval=1)
        plt.show()
        return;

test = generateFrameSet.generateFrameSet("*.tif")

animation = contourMapAnim(test)

animation.startAnim()

r = ctrmap.contourMap(test[0])

sys.stdout = open('log.txt', 'w')

print(test[0])
print(test[0].shape)

sys.stdout.close()
