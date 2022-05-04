import pandas as pd
from SleepQuality.Libraries.StatusCalculation import reportLawStatus
from SleepQuality.Libraries.AuxiliaryFunction import createNewStatusList
from SleepQuality.Libraries.AuxiliaryFunction import identifyMedian
from SleepQuality.Libraries.notProcessedFile import csvFile

#This file process data considering different types of filter window in the windowToTest array
#A parameter is also the median window, better mantain 5 as value

def outputFileName(file):
  file = file[:-4]
  file = file + "_Good10Sample.csv"
  return file

windowToTest = [150, 120, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
medianWindow = 10
statusGroup = createNewStatusList(windowToTest)

for numFile in range(len(csvFile)):
  print(csvFile[numFile])
  beginData = pd.read_csv(csvFile[numFile], sep=";")
  beginData = beginData.dropna(how="any", axis=0)
  beginData = beginData.reset_index()

  data = pd.DataFrame()
  for status in statusGroup:
    output = []
    output = identifyMedian(beginData['status'], medianWindow)
    data['status'] = output
  data = data.reset_index()
  data['id'] = data.index

  for newStatus, windowDim in statusGroup.items():
    print("Elaborating", newStatus, "...")
    data[newStatus]=data.apply(lambda row: reportLawStatus(data, row, windowDim, 0.8), axis=1)

  data.to_csv(outputFileName(csvFile[numFile]), encoding='utf-8')

