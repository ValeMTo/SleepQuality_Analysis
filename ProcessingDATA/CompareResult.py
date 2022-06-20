import pandas as pd
from matplotlib import pyplot as plt

from SleepQuality.Libraries.StatusCalculation import reportLawStatus
from SleepQuality.Libraries.AuxiliaryFunction import identifyMedian
from SleepQuality.Libraries.notProcessedFile import csvFile
from SleepQuality.Libraries.AwakeFunction import awakeBeginningMoment
from SleepQuality.Libraries.PlotFunction import createGraphOf

#("..\..\Archivio\EachSecond\\bed_raw_2022-03-24_60-F1-89-29-82-44.csv")
csvFile = csvFile
medianWindow = 5

dataToPrint = pd.DataFrame()
for numFile in range(len(csvFile)):
  name = csvFile[numFile][40:45]
  print("Elaborating...", name)
  beginData = pd.read_csv(csvFile[numFile], sep=";")
  beginData = beginData.dropna(how="any", axis=0)
  beginData = beginData.reset_index()

  data = pd.DataFrame()
  output = []
  output = identifyMedian(beginData['status'], medianWindow)
  data['status'] = output
  data = data.reset_index()
  data['id'] = data.index
  dataToPrint[name]=data.apply(lambda row: reportLawStatus(data, row, 75, 0.8), axis=1)
  awake = awakeBeginningMoment(dataToPrint[name])
  print(awake[1:])
  createGraphOf(name, dataToPrint, 5)


dataToPrint = dataToPrint.reset_index()
dataToPrint['id'] = dataToPrint.index
data.to_csv(".\\allData75.csv", encoding='utf-8')
plt.show()

