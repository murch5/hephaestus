import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#import hgvs.parser as hgvsparser
from plotmanager.plottype import track


class VariantTrack(track.Track):

    def __init__(self,figure, data, plot_XML):
        track.Track.__init__(self,figure, data, plot_XML)
        self.variants = self.data.getFeature("variant")

        self.featureLabel = "Note"

    def draw(self):

        self.trackAnnotations()

        self.subplot.set_ylim([0.5, 1.5])
        self.subplot.title.set_text("")
        self.subplot.axis("off")


        return;

    def parseHGVS(self):
        return
