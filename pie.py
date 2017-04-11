import animPlot as animPlot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class pie(animPlot.animPlot):

    def __init__(self, figure, data, position, title="",plotArgs=[],annotate=[]):
        animPlot.animPlot.__init__(self, figure, data, position,title, plotArgs,annotate)
        self.explode = self.retrieveArgVal("explode")
        self.NaNindices = self.data.isnull()
        self.numNan = np.sum(self.NaNindices)
        self.dataCleaned = self.data[self.data.notnull()]
        self.labels = pd.DataFrame(self.dataCleaned.index.tolist())
        print(self.labels)
        self.labels.columns = ["Labels"]
        self.pctFilter = 1

        self.colors = ["#6a6dc5","#76b74b","#a656c4","#68803b","#c666a8","#4eb596","#ca5938","#689bd6","#c49643","#ca586f"]
        return

    def animate(self,i):
        return


    def draw(self):

        def make_autopct(values):
            def my_autopct(pct):

                total = values.sum()
                if(isinstance(total,pd.Series)):
                    total = total.values
                    total = total[0]
                    pct = pct[0]
                else:
                    total = total

                val=int((pct*total/100.0)+0.5)

                if self.retrieveArgVal("show%") is not None:
                    wedgeLabel = '{p:.2f}%  ({v:d})'.format(p=pct, v=val) if pct > self.pctFilter else ''
                else:
                    wedgeLabel = '({v:d})'.format(v=val) if pct > self.pctFilter else ''

                return wedgeLabel

            return my_autopct

        if self.retrieveArgVal("pctFilter") is not None:
            self.pctFilter = int(self.retrieveArgVal("pctFilter"))

        if self.retrieveArgVal("hideLabelByVal") is not None:

            data = self.dataCleaned
            hiddenVal = data.to_frame(name="val").query(self.retrieveArgVal("hideLabelByVal"))


            labelsToKeep = hiddenVal.index.tolist()
            if labelsToKeep is not None:
                self.labels.replace(labelsToKeep," ",inplace=True)

        if len(self.dataCleaned) % 2 == 0:
            colorWedge = ["#9F4298", "#D1AFD3"]
        else:
            colorWedge = ["#9F4298", "#D1AFD3","#E6E7E8"]

        if self.explode != 0 and self.explode != -1:
            self.subplot.pie(self.dataCleaned,labels=self.labels.ix[:,0], startangle=90, explode=self.explode, autopct=make_autopct(self.dataCleaned),colors=colorWedge)
        else:
            self.subplot.pie(self.dataCleaned, labels=self.labels.ix[:,0], startangle=90,autopct=make_autopct(self.dataCleaned),colors=colorWedge)

        self.subplot.axis("equal")

        return

    def initAnimate(self, i):
        return

