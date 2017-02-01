
import animPlot as animPlot
import numpy as np
import pandas as pd

#data format:  [Label,Odds Ratio,Lower Confidence Interval, Upper Confidence Interval]
class forest(animPlot.animPlot):

    def __init__(self, figure, data, position,title=""):
        animPlot.animPlot.__init__(self, figure, data, position,title)

        self.initializeForest()

        return
    def draw(self):
        return
    def initAnimate(self):
        print(0)
        return
    def animate(self):
        print(0)
        return
    def initializeForest(self):


        Y = np.arange(len(self.data.index))
        print(self.data)
        self.subplot.plot(self.data.ix[:,1],Y,"rh")

        for index,row in self.data.iterrows():
          #  self.subplot.plot(dataRo)

            print(row)
            print(row[2:4])
            print(Y[index])
            yCoord = [Y[index],Y[index]]
            self.subplot.plot(row[2:4], yCoord, "r-")

        self.subplot.set_yticks(Y)
        self.subplot.grid(axis="y")
        self.subplot.set_yticklabels(self.data.ix[:,0])
        self.subplot.set_xlabel("Odds Ratio")

        #print(Y)
        return

