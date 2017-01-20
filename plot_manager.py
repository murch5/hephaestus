import matplotlib.pyplot as plt
from imageStack import imageStack
from violin import violin
import generateFrameSet as gf
import matplotlib.animation as anim
plt.rcParams['animation.ffmpeg_path'] = '/ffmpeg/bin/ffmpeg'

class plot_manager():

    def __init__(self):
        self.figure = plt.figure(figsize=(8, 4))
        self.plotList = []
        self.animHandler = None
        self.writer = None
        self.framesPerImage = 1
        self.totalFrames = 80
        self.currFrameIndex = 0
        self.currImageIndex = 0
        self.saveAnimFlag = False

        return;



    def addPlot(self,plotClass,data, position):

        newPlot = plotClass(self.figure,data, position)
        print(newPlot)
        self.plotList.append(newPlot)


    def startAnim(self):
        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')
        self.saveAnimFlag = True
        self.animHandler = anim.FuncAnimation(self.figure, self.animatePlot, frames=self.framesPerImage * self.totalFrames, init_func=self.initAnim)
        if self.saveAnimFlag == True: self.saveAnimationToFile()
        plt.show()
        return;

    def saveAnimationToFile(self):


        self.writer = anim.FFMpegWriter(fps=15, bitrate=5000)
        self.animHandler.save("t.mp4",writer=self.writer)
        return;

    def initAnim(self):

        return;

    def animatePlot(self,i):

        for plot in self.plotList:
            plot.animate(i)
            plot.drawText()
        return;

    def getFigure(self):
        return self.figure;

    def addLabel(self,text,position,colorMap,index):
        self.plotList[index].addTextAnnotation(text,position,colorMap)
        return;

    def drawPlots(self):

        for plot in self.plotList:
            plot.draw()

        plt.show()
        return;



test1 = plot_manager()
test1.addPlot(violin,((2,2,3,2,4,6,2),(1,2,2,2,1,1,1)),211)
test1.addPlot(violin,((1,2,2,2,1,1,1),(2,2,3,2,4,6,2)),212)
test1.drawPlots()
