from plotmanager.plottype import anim_plot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Pie(anim_plot.AnimPlot):

    def __init__(self,figure, data, plot_XML):
        anim_plot.AnimPlot.__init__(self, figure, data, plot_XML)
        self.explode = None
        self.labels = pd.DataFrame(self.data.get().index.tolist())
        self.labels.columns = ["Labels"]

        self.pct_filter = 1
        self.type = "pie"
        self.colors = ["#6a6dc5","#76b74b","#a656c4","#68803b","#c666a8","#4eb596","#ca5938","#689bd6","#c49643","#ca586f"]

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

                if self.get_set_param("show_pct")==True:
                    wedgeLabel = '{p:.2f}%  ({v:d})'.format(p=pct, v=val) if pct > self.get_set_param("pct_filter") else ''
                else:
                    wedgeLabel = '({v:d})'.format(v=val) if pct > self.pct_filter else ''

                return wedgeLabel

            return my_autopct


        if self.checkXML(".//plot_style//hide_labels_byvalue"):
            threshold = self.getXMLvalue(".//plot_style//hide_labels_byvalue")
            hiddenVal = self.data.get().to_frame(name="val").query("val"+ threshold)
            print(hiddenVal)
            labelsToKeep = hiddenVal.index.tolist()
            print(labelsToKeep)
            if labelsToKeep is not None:
                self.labels.replace(labelsToKeep," ",inplace=True)

        if len(self.data.get()) % 2 == 0:
            colorWedge = ["#9F4298", "#D1AFD3"]
        else:
            colorWedge = ["#9F4298", "#D1AFD3","#E6E7E8"]

        self.subplot.pie(self.data.get(),labels=self.labels.ix[:,0], startangle=90, explode=self.explode, autopct=make_autopct(self.data.get()),colors=colorWedge)

        self.subplot.axis("equal")

        return

