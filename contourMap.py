import matplotlib.pyplot as plt
import numpy as np
import sys

import generateFrameSet


def initContourMap(topologyData):

    dim = topologyData.shape

    return;

test = generateFrameSet.generateFrameSet("*.tif")

sys.stdout = open('log.txt', 'w')

print(test[0])
print(test[0].shape)

sys.stdout.close()
