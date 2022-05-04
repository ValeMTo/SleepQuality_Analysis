from SleepQuality.Libraries.AwakeFunction import awakeBeginningMoment
import numpy
import matplotlib.pyplot as plt
import pandas as pd

def createGraphOf(window, file, numSamplesMedian ):
  newStatus = 'newStatus' + str(window)
  print(newStatus)
  data = pd.read_csv(file, sep=",")

  statusPoints = numpy.copy(data.loc[data[newStatus] == 0].index)

  finalStatusPoints = []
  for cell in statusPoints:
    for i in range(numSamplesMedian):
      finalStatusPoints.append(numSamplesMedian*cell+i)

  statusLevelPoints = [newStatus] * statusPoints.size * numSamplesMedian
  plt.scatter(finalStatusPoints, statusLevelPoints, marker=".")

  print(awakeBeginningMoment(finalStatusPoints))

def createGraphOfStatus(file):
  data = pd.read_csv(file, sep=",")
  statusPoints = numpy.copy(data.loc[data['status'] == 0].index)
  statusLevelPoints = ['status'] * statusPoints.size
  plt.scatter(statusPoints, statusLevelPoints, marker=".")