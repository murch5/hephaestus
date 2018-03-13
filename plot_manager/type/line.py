
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from type import anim_plot


class Line(anim_plot.AnimPlot):

    def draw(self):

        if len(self.data[0].shape) == 1:
            self.subplot.plot(self.data[0], "-")
        elif len(self.data[0].shape) == 2:
            self.subplot.plot(self.data[0].ix[:, 0],self.data[0].ix[:, 1],"-")
        elif len(self.data[0].shape) > 2:
            for i in range(1,len(self.data[0].shape)):
                self.subplot.plot(self.data[0].ix[:, 0], self.data[0].ix[:, i], "-")

        self.subplot.semilogy()
        pass