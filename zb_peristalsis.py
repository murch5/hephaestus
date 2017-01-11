import contourMapAnim as cm
import generateFrameSet as gf

class zbPeristalsis():

    def loadBoundaryCoord(fileName):
        return;

    def drawBoundaryCoord(self):
        self.contourAnimationHandler.contourMapBase.assignLineDrawFunc("")

        return;

    def __init__(self):
        self.contourAnimationHandler = cm.contourMapAnim(gf.generateFrameSet("*.tif"))
        self.contourAnimationHandler.startAnim()

        self.drawBoundaryCoord()



test = zbPeristalsis()

