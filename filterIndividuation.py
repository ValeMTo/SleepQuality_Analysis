
# The goal is to find the best filter window.
# When can we be sure of the awake action?

import pandas as pd
import numpy
import matplotlib.pyplot as plt
from SleepQuality.AwakeFunction import awakeIntoGroups
from SleepQuality.AuxiliaryFunction import createNewStatusList

csvFile = []
csvFile.append("..\Archivio\EachSecond\\bed_raw_2022-03-24_60-F1-89-29-82-44_elaborated.csv")
csvFile.append("..\Archivio\EachSecond\\bed_raw_2022-03-25_60-F1-89-29-82-44_elaborated.csv")
csvFile.append("..\Archivio\EachSecond\\bed_raw_2022-03-26_60-F1-89-29-82-44_elaborated.csv")
csvFile.append("..\Archivio\EachSecond\\bed_raw_2022-03-27_60-F1-89-29-82-44_elaborated.csv")
csvFile.append("..\Archivio\EachSecond\\bed_raw_2022-03-28_60-F1-89-29-82-44_elaborated.csv")

windowToTest = [180, 120, 100, 90, 60, 30, 20, 15, 10, 5]
statusGroup = createNewStatusList(windowToTest)
for numFile in range(1):
  data = pd.read_csv(csvFile[numFile], sep=",")

  data =  data.tail(-30000)

  statusLevel = 2
  awakeGroups = awakeIntoGroups(data, "status")
  print(awakeGroups)
  statusPoints = numpy.copy(data.loc[data["status"] == 0].index)
  statusLevelPoints = numpy.full(statusPoints.size, statusLevel)
  plt.scatter(statusPoints, statusLevelPoints, marker=".")
  for newStatus, windowDim in statusGroup.items():
    awakeGroups = awakeIntoGroups(data, newStatus)
    print(awakeGroups)

    statusLevel += 2
    statusPoints = numpy.copy(data.loc[data[newStatus] == 0].index)
    statusLevelPoints = numpy.full(statusPoints.size, statusLevel)
    plt.scatter(statusPoints, statusLevelPoints, marker=".")

  plt.show()

