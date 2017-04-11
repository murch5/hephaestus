import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import track as track


class DNAtrack(track.track):
    def __init__(self, figure, data, position, title="", plotArgs=[], annotate=[]):
        track.track.__init__(self, figure, data, position, title, plotArgs, annotate)
        self.features = self.data.getFeature("exon")
        self.chainLimits = self.data.getChain("region")
        self.featureLabel = "ID"