import matplotlib.pyplot as plt
from zb_peristalsis import zbPeristalsis
import generateFrameSet as gf
import matplotlib.animation as anim

class plot_manager():

    def __init__(self):
        self.figure = plt.figure()
        self.plotList = []
        self.animHandler = []
        self.framesPerImage = 1
        self.totalFrames = 80
        self.currFrameIndex = 0
        self.currImageIndex = 0

        return;

    def addPlot(self,plotClass,data, position):

        newPlot = plotClass(self.figure,data, position)
        print(newPlot)
        self.plotList.append(newPlot)


    def startAnim(self):
        self.animHandler = anim.FuncAnimation(self.figure, self.animate, frames=self.framesPerImage * self.totalFrames, init_func=self.initAnim)
        plt.show()
        return;

    def initAnim(self):

        return;

    def animate(self):

        #for plot in plotList:


        return;

    def getFigure(self):
        return self.figure;


test1 = plot_manager()
test1.addPlot(zbPeristalsis,gf.generateFrameSet("*.tif"),211)
test1.addPlot(zbPeristalsis,gf.generateFrameSet("*.tif"),222)

test1.startAnim()
#test = zbPeristalsis(test1.getFigure(),gf.generateFrameSet("*.tif"),111)