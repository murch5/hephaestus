import contourMapAnim
import generateFrameSet

class zbPeristalsis():

    def __init__(self):
        self.contourAnimationHandler = contourMapAnim.contourMapAnim(generateFrameSet.generateFrameSet("*.tif"))
        self.contourAnimationHandler.startAnim()

test = zbPeristalsis()
