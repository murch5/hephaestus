
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from plot_manager.type import anim_plot


class Line(anim_plot.AnimPlot):

    def draw(self):


      #  if isinstance(self.data[0],np.ndarray):
          #  self.data[0] = pd.DataFrame(self.data[0])
           # print("test")
        #print(self.data[0].shape)

        print(len(self.data[0].shape))
        if len(self.data[0].shape) == 1:
            self.subplot.plot(self.data[0], "-")
        elif len(self.data[0].shape) == 2:
            self.subplot.plot(self.data[0].ix[:, 0],self.data[0].ix[:, 1],"-")
        elif len(self.data[0].shape) > 2:
            for i in range(1,len(self.data[0].shape)):
                self.subplot.plot(self.data[0].ix[:, 0], self.data[0].ix[:, i], "-")

        self.subplot.semilogy()
        pass