import pandas as pd

from SleepQuality.Libraries.AuxiliaryFunction import createNewStatusAwakeRange
from SleepQuality.Libraries.AuxiliaryFunction import identifyMedian
from SleepQuality.Libraries.StatusCalculation import reportLawStatus
from SleepQuality.Libraries.notProcessedFile import csvFile

#This file process data considering different types of awakeParameter in the awakeToTest array
#A parameter is also the median window, better mantain 5 as value

def outputFileName(file):
  file = file[:-4]
  file = file + "_complex5Sample.csv"
  return file

awakeToTest = [0.6, 0.7, 0.8, 0.9, 1]
medianWindow = 5

statusGroup = createNewStatusAwakeRange(75, awakeToTest)

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

  for newStatus, awakeValue in statusGroup.items():
    print("Elaborating", newStatus, "...")
    data[newStatus] = data.apply(lambda row: reportLawStatus(data, row, 75, awakeValue), axis=1)

  data.to_csv(outputFileName(csvFile[numFile]), encoding='utf-8')
