import contourMap

class contourMapAnim():

    def __init__(self, frames):
        self.contourMapBase = contourMap(frames[0])
        self.frames = frames

        return;

    test = generateFrameSet.generateFrameSet("*.tif")

    r = contourMap(test[0])

    sys.stdout = open('log.txt', 'w')

    print(test[0])
    print(test[0].shape)

    sys.stdout.close()
