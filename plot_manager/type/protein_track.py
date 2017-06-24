import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from plot_manager.type import track


class ProteinTrack(track.Track):

    def __init__(self,figure, data, plot_settings):
        track.Track.__init__(self,figure, data, plot_settings)
        self.features = self.data.getFeature("Repeat")
        self.chainLimits = self.data.getChain("Chain")
        self.featureLabel = "Note"