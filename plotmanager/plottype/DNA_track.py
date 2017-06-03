import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from plotmanager.plottype import track


class DNAtrack(track.Track):
    def __init__(self,figure, data, plot_XML):
        track.Track.__init__(self,figure, data, plot_XML)
        self.features = self.data.getFeature("exon")
        self.chainLimits = self.data.getChain("region")
        self.featureLabel = "ID"