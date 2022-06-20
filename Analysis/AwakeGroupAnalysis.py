
# The goal is to find the best filter window.
# When can we be sure of the awake action?

import pandas as pd
import numpy
import matplotlib.pyplot as plt
from SleepQuality.Libraries.AwakeFunction import awakeIntoGroups
from SleepQuality.Libraries.AuxiliaryFunction import createNewStatusList
from SleepQuality.Libraries.notProcessedFile import allCsvFiles

csvFile = allCsvFiles

windowToTest = [150, 120, 100, 90, 60, 50, 40, 30, 20, 10]
statusGroup = createNewStatusList(windowToTest)
completeStatusGroup = list(statusGroup.values())
completeStatusGroup = list(map(str, completeStatusGroup))
completeStatusGroup.insert(0, "Original")
for numFile in range(len(allCsvFiles)):
  print(csvFile[numFile])
  numAwakeGroups = []
  data = pd.read_csv(csvFile[numFile], sep=",")

  statusLevel = 2
  awakeGroups= awakeIntoGroups(data, "status")
  numAwakeGroups.append(len(awakeGroups))

  statusPoints = numpy.copy(data.loc[data["status"] == 0].index)
  statusLevelPoints = ["status"] * statusPoints.size
  plt.scatter(statusPoints, statusLevelPoints, marker=".")
  for newStatus, windowDim in statusGroup.items():
    awakeGroups = awakeIntoGroups(data, newStatus)
    numAwakeGroups.append(len(awakeGroups))

    statusLevel += 2
    statusPoints = numpy.copy(data.loc[data[newStatus] == 0].index)
    statusLevelPoints = [newStatus] * statusPoints.size

  plt.ylabel("Number of awake groups")
  plt.title("Comparison of number of awake groups")
  print(numAwakeGroups)
  plt.bar(completeStatusGroup, numAwakeGroups)
  plt.show()