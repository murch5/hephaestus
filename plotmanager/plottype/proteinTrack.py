import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from plotmanager.plottype import track


class ProteinTrack(track.Track):

    def __init__(self,figure, data, plot_XML):
        track.Track.__init__(self,figure, data, plot_XML)
        self.features = self.data.getFeature("Repeat")
        self.chainLimits = self.data.getChain("Chain")
        self.featureLabel = "Note"