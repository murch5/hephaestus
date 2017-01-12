import matplotlib.pyplot as plt


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

    def addPlot(self,plotClass, position):

        newPlot = plotClass(data, position)
        self.subplotList.append(newSubplot)

    def startAnim(self):
        self.animHandler = anim.FuncAnimation(self.figure, self.animate, frames=self.framesPerImage * totalFrames, init_func=self.initAnim)
        plt.show()
        return;

    def initAnim(self):

        return;

    def animate(self):

        #for plot in plotList:


        return;

    def getFigure(self):
        return self.figure;