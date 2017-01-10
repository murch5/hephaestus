import contourMap as ctrmap
import generateFrameSet
import sys

class contourMapAnim():

    def __init__(self, frames):
        self.contourMapBase = ctrmap.contourMap(frames[0])
        self.frames = frames

        return;

    def animateContour(n):
        return;

    def animateInit(self):
        return;

test = generateFrameSet.generateFrameSet("*.tif")

animation = contourMapAnim(test)

r = ctrmap.contourMap(test[0])

sys.stdout = open('log.txt', 'w')

print(test[0])
print(test[0].shape)

sys.stdout.close()
