import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from plotmanager.plottype import track


class proteinTrack(track.track):

    def __init__(self,figure, data, position,title="",plotArgs=[],annotate=[]):
        track.track.__init__(self, figure, data, position, title, plotArgs, annotate)
        self.features = self.data.getFeature("Repeat")
        self.chainLimits = self.data.getChain("Chain")
        self.featureLabel = "Note"