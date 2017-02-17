import matplotlib.gridspec as gridspec
import pandas as pd
import numpy as np

class textAnnotate():
    def __init__(self,text,position,colorMap):
        self.text = text
        self.position = position
        self.colorMap = colorMap
        self.argList = []


    def getText(self):
        return self.text;

    def getPosition(self):
        return self.position;

    def getColorMap(self):
        return self.colorMap;

class plot():

    def __init__(self,figure, data, position, title, plotArgs=[]):
        self.figure = figure
        self.data = data[:]
        self.position = position
        self.gridSpec = []
        self.argFlag = False
        self.argList = self.parseArgs(plotArgs)
        self.showX = True
        self.showY = True
        self.invertX = False
        self.invertY = False
        self.showYlabels = True
        self.showXlabels = True
        self.showTitle = True
        self.insetLabel = False





        self.subplot = self.setupSubplot()

        #self.subplot = figure.add_subplot(position, aspect="equal")

        #self.subplot = figure.add_subplot(self.gridSpec[int(self.position[2]),int(self.position[3])])
        self.txtAnnotations = []
        self.plotTitle = title

        if self.retrieveArgVal("insetLabel") is not None: self.insetLabel = True

        print(self.retrieveArgVal("hideTitle"))
        if self.retrieveArgVal("hideTitle") is not None: self.showTitle = False

        if self.showTitle == True: self.subplot.title.set_text(self.plotTitle)

        if self.showTitle == False: self.subplot.title.set_text("")

        if self.retrieveArgVal("hideX") is not None: self.showX = False
        if self.retrieveArgVal("hideY") is not None: self.showY = False

        if self.retrieveArgVal("invertX") is not None: self.invertX = True; self.subplot.invert_xaxis()
        if self.retrieveArgVal("invertY") is not None: self.invertY = True; self.subplot.invert_yaxis()

        self.subplot.get_xaxis().set_visible(self.showX)
        self.subplot.get_yaxis().set_visible(self.showY)

        if self.showXlabels == False: self.subplot.axes.get_xaxis().set_ticklabels([])
        if self.showYlabels == False: self.subplot.axes.get_yaxis().set_ticklabels([])


        if self.retrieveArgVal("xlim") is not None:
            self.xlim = np.fromstring(self.retrieveArgVal("xlim"),sep=":")
        else:
            self.xlim = []
        if self.retrieveArgVal("ylim") is not None:
            self.ylim = np.fromstring(self.retrieveArgVal("ylim"),sep=":")
        else:
            self.ylim = []



    def animate(self,i):
        return;

    def initAnimate(self, i):
        return;

    def draw(self):
        return;

    def init(self):
        return;

    def drawText(self):
        for text in self.txtAnnotations:
            self.subplot.annotate(text.getText(),text.getPosition(),color=text.getColorMap(),size=15)
        return;

    def addTextAnnotation(self,text,position,colorMap):
        newAnnotate = textAnnotate(text,position,colorMap)
        self.txtAnnotations.append(newAnnotate)
        return;

    def getData(self):
        return self.data

    def setupSubplot(self):

        self.gridSpec = gridspec.GridSpec(int(self.position[0]),int(self.position[1]))

        subplotspec = self.gridSpec.new_subplotspec([int(self.position[2]),int(self.position[3])], int(self.position[4]), int(self.position[5]))

        subplotNew = self.figure.add_subplot(subplotspec)

        return subplotNew

    def parseArgs(self, args):

        argPD = pd.Series(args)
        argList = []
        if argPD.any():
            for i in argPD:

                if i!=0:
                    q = i.split("=", 1)
                    argList.append(q)

        if(len(argList)>0):

            if argList[0][0]!="0":
                argList = dict(argList)
                self.argFlag = True
            else:
                argList = {0:0}
        else:
            argList = {0: 0}

        return argList

    def retrieveArgVal(self,argID):

        return self.argList.get(argID)

