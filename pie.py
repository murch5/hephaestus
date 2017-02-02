import animPlot as animPlot
import numpy as np
import pandas as pd

class pie(animPlot.animPlot):

    def __init__(self, figure, data, position, title="", explode=0):
        animPlot.animPlot.__init__(self, figure, data, position,title)
        self.explode = explode
        self.NaNindices = self.data.isnull()
        self.numNan = np.sum(self.NaNindices)
        self.dataCleaned = self.data[self.data.notnull()]

        print(self.dataCleaned)
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

                print(type(pct))
                print(type(val))
                temp = '{p:.2f}%  ({v:d})'.format(p=pct, v=val) if pct > 1 else ''

                return '{p:.2f}%  ({v:d})'.format(p=pct, v=val) if pct > 1 else ''

            return my_autopct



        if self.explode != 0:
            self.subplot.pie(self.dataCleaned,labels=list(self.dataCleaned.index), startangle=90, explode=self.explode, autopct=make_autopct(self.dataCleaned))
        else:
            self.subplot.pie(self.dataCleaned, labels=list(self.dataCleaned.index), startangle=90,autopct=make_autopct(self.dataCleaned))

        self.subplot.axis("equal")

        return

    def initAnimate(self, i):
        return

