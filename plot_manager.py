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
        self.animHandler = anim.FuncAnimation(self.figure, self.animatePlot, frames=self.framesPerImage * self.totalFrames, init_func=self.initAnim)
        plt.show()
        return;

    def initAnim(self):

        return;

    def animatePlot(self,i):

        for plot in self.plotList:
            plot.animate(i)


        return;

    def getFigure(self):
        return self.figure;


test1 = plot_manager()
test1.addPlot(zbPeristalsis,gf.generateFrameSet("*.tif"),121)
test1.addPlot(zbPeristalsis,gf.generateFrameSet("*.tif"),122)
test1.addPlot(zbPeristalsis,gf.generateFrameSet("*.tif"),222)

test1.startAnim()
#test = zbPeristalsis(test1.getFigure(),gf.generateFrameSet("*.tif"),111)