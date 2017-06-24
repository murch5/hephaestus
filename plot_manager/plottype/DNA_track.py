import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from plot_manager.plottype import track


class DNAtrack(track.Track):
    def __init__(self,figure, data, plot_settings):
        track.Track.__init__(self,figure, data, plot_settings)
        self.features = self.data.getFeature("exon")
        self.chainLimits = self.data.getChain("region")
        self.featureLabel = "ID"