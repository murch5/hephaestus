import contourMapAnim as cm
import generateFrameSet as gf

class zbPeristalsis():

    def __init__(self):
        self.contourAnimationHandler = cm.contourMapAnim(gf.generateFrameSet("*.tif"))
        self.contourAnimationHandler.startAnim()

    def loadBoundaryCoord(fileName):

        return;

    #def drawBoundaryCoord
test = zbPeristalsis()
