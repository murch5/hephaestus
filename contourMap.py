import matplotlib.pyplot as plt
import numpy as np
import sys
import scipy as sp

import generateFrameSet

class contourMap:

    x, y, X, Y = []

    def __init__(self,data):
        self.surfaceData = data
        return;

    def initContourMap(topologyData):

        dim = topologyData.shape
        print(dim)

        x = np.arange(0, dim[0])
        y = np.arange(0, dim[1])

        return;

test = generateFrameSet.generateFrameSet("*.tif")

r = contourMap(test)

sys.stdout = open('log.txt', 'w')

print(test[0])
print(test[0].shape)

sys.stdout.close()
