import seaborn as sb
import matplotlib.pyplot as plt

from type import anim_plot


class Histogram(anim_plot.AnimPlot):
    def draw(self):

        sb.color_palette("muted")

        if (len(self.data[0].columns) == 3):
            self.subplot = sb.violinplot(x=self.data[0].iloc[:, 0], y=self.data[0].iloc[:, 1],
                                         hue=self.data[0].iloc[:, 2], split=True, ax=self.subplot, orient=self.orient,
                                         cut=self.cut, scale=self.scale, inner=self.inner)
        else:
            self.subplot = sb.violinplot(x=self.data[0].iloc[:, 0], y=self.data[0].iloc[:, 1], ax=self.subplot,
                                         orient=self.orient, cut=self.cut, scale=self.scale, inner=self.inner)

        self.subplot.yaxis.label.set_size(14)
        self.subplot.xaxis.label.set_size(14)

        ticks_x = self.subplot.xaxis.get_major_ticks()

        for tick in self.subplot.xaxis.get_major_ticks():
            tick.label.set_fontsize(14)

        for tick in self.subplot.yaxis.get_major_ticks():
                tick.label.set_fontsize(14)

        for i,tick in enumerate(self.subplot.xaxis.get_majorticklocs()):
            if tick < 0:

                ticks_x[i].set_visible(False)




           # print(tick.get_loc())
        return
