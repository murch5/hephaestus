

class textAnnotate():
    def __init__(self,text,position,colorMap):
        self.text = text
        self.position = position
        self.colorMap = colorMap

    def getText(self):
        return self.text;

    def getPosition(self):
        return self.position;

    def getColorMap(self):
        return self.colorMap;

class plot():

    def __init__(self,figure, data, position, title):
        self.figure = figure
        self.data = data
        self.position = position
        #self.subplot = figure.add_subplot(position, aspect="equal")
        self.subplot = figure.add_subplot(position)
        self.txtAnnotations = []
        self.plotTitle = title

        self.subplot.title.set_text(self.plotTitle)

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


