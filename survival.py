import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import lifelines as lifelines

import animPlot as animPlot
import matplotlib.colors as colors


class survival(animPlot.animPlot):


    def __init__(self,figure,data,position, title="",plotArgs=[],annotate=[]):
        animPlot.animPlot.__init__(self,figure,data,position,title,plotArgs,annotate)
        self.type = "KaplanMeier"

        self.survivalData = self.generateSurvivalData()

    def draw(self):
        colorWedge = ["#9F4298", "#D1AFD3"]

        if self.retrieveArgVal("aafpredictsurvival") is not None:
            self.survivalData.predict_survival_function(self.data.ix[1:15]).plot(ax=self.subplot)
        else:
            self.survivalData.plot(ax=self.subplot,color=colors.hex2color("#9F4298"))


        #sb.regplot(x=self.data.ix[:,0],y=self.data.ix[:, 1],fit_reg=True,ax=self.subplot)

        self.setPlotLevelProperties()

        return

    def initAnimate(self):
        print(0)
    def animate(self):
        print(0)

    def generateSurvivalData(self):

        kmf = lifelines.KaplanMeierFitter()
        naf = lifelines.NelsonAalenFitter()
        print(self.data)

        print(self.data.ix[:,0])


        if(self.data.shape[1] > 2):

            cf = lifelines.CoxPHFitter()
            self.data.columns.values[0] = "T"
            self.data.columns.values[1] = "E"
            print(self.data)
            cf.fit(self.data, "T", event_col="E")
            cf.print_summary()

            aaf = lifelines.AalenAdditiveFitter(fit_intercept=False)
            aaf.fit(self.data, 'T', event_col='E')


            kmf = aaf
        else:

            kmf.fit(self.data.ix[:,0],self.data.ix[:,1])
            naf.fit(self.data.ix[:,0],self.data.ix[:,1])

        if self.retrieveArgVal("naf") is not None: kmf = naf

        return kmf