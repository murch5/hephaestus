from plot_manager.type import anim_plot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Pie(anim_plot.AnimPlot):

    def draw(self):

        print(self.colors)
        self.explode = None

        self.labels = pd.DataFrame(self.data[0].index.tolist())
        print(self.labels)
        self.labels.columns = ["Labels"]

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

                if self.show_pct:
                    wedgeLabel = '{p:.2f}%  ({v:d})'.format(p=pct, v=val) if pct > self.pct_filter else ''
                else:
                    wedgeLabel = '({v:d})'.format(v=val) if pct > self.pct_filter else ''

                return wedgeLabel

            return my_autopct


        if self.get("hide_label_by_value"):

            threshold = self.get("hide_label_by_value")
            hiddenVal = self.data[0].to_frame(name="val").query("val"+ threshold)
            print(hiddenVal)
            labelsToKeep = hiddenVal.index.tolist()
            print(labelsToKeep)
            if labelsToKeep is not None:
                self.labels.replace(labelsToKeep," ",inplace=True)

        if len(self.data[0]) % 2 == 0:
            color_wedge = ["#9F4298", "#D1AFD3"]
        else:
            color_wedge = ["#9F4298", "#D1AFD3","#E6E7E8"]

        self.subplot.pie(self.data[0],labels=self.labels.ix[:,0], startangle=90, explode=self.explode, autopct=make_autopct(self.data[0]),colors=color_wedge)

        self.subplot.axis("equal")

        return

