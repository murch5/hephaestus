from plot_manager.type import anim_plot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Pie(anim_plot.AnimPlot):
    def draw(self):


        self.explode = None

        self.labels = pd.DataFrame(self.data[0].index.tolist())

        self.labels.columns = ["Labels"]

        def make_autopct(values):
            def my_autopct(pct):

                total = values.sum()
                if (isinstance(total, pd.Series)):
                    total = total.values
                    total = total[0]
                    pct = pct[0]
                else:
                    total = total

                val = int((pct * total / 100.0) + 0.5)

                if self.show_pct:
                    wedgeLabel = '{p:.2f}%  ({v:d})'.format(p=pct, v=val) if pct > self.pct_filter else ''
                else:
                    wedgeLabel = '({v:d})'.format(v=val) if pct > self.pct_filter else ''

                return wedgeLabel

            return my_autopct

        if self.get("hide_label_by_value"):

            threshold = self.get("hide_label_by_value")
            hiddenVal = self.data[0].to_frame(name="val").query("val" + threshold)
            print(hiddenVal)
            labelsToKeep = hiddenVal.index.tolist()
            print(labelsToKeep)
            if labelsToKeep is not None:
                self.labels.replace(labelsToKeep, " ", inplace=True)

                # seaborn_muted = ["#4878CF", "#6ACC65", "#D65F5F",
                # "#B47CC7", "#C4AD66", "#77BEDB"],

        if len(self.data[0]) % 2 == 0:
            color_wedge = ["#2D75A2", "#E0812B"]
        else:
            color_wedge = ["#2D75A2", "#E0812B", "#3A923A"]

        patches, text, autotext = self.subplot.pie(self.data[0], labels=self.labels.ix[:, 0], startangle=90,
                                                   explode=self.explode, autopct=make_autopct(self.data[0]),
                                                   colors=color_wedge, wedgeprops={"linewidth":1, "ec":"black"})

        for label in autotext:
            label.set(fontsize=13)
            label.set_bbox({"facecolor":"white","alpha":0.75})


        for label in text:
            label.set(fontsize=16)

        self.subplot.axis("equal")

        return
