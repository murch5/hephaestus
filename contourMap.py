import matplotlib.pyplot as plt
import numpy as np
import sys
import scipy as sp

import generateFrameSet

class contourMap:

    def __init__(self):
        return;



def initContourMap(topologyData):

    dim = topologyData.shape
    print(dim)
    return;

test = generateFrameSet.generateFrameSet("*.tif")

initContourMap(test[0])

sys.stdout = open('log.txt', 'w')

print(test[0])
print(test[0].shape)

sys.stdout.close()
