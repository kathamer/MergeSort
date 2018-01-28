"""
Data.py
Handles generation of sample data for sorting algorithyms
by Dylan Hamer
"""

import random
import time

def generateSample(**kwargs):
    dataset = []
    randomSeed = kwargs.get("seed", time.time())
    datasetSize = kwargs.get("size", 10000)
    minimumValue = kwargs.get("minimumValue", 0)
    maximumValue = kwargs.get("maximumValue", 10000)

    random.seed(randomSeed)

    for index in range(datasetSize):
        print("Generating data set ({}/{})...".format(index, datasetSize))
        dataset.append(random.randint(minimumValue, maximumValue))
    print("Done")

    return dataset

