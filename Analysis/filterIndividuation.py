
# The goal is to find the best filter window.
# When can we be sure of the awake action?

import pandas as pd
import numpy
import matplotlib.pyplot as plt
import xlsxwriter
from SleepQuality.Libraries.AwakeFunction import awakeIntoGroups
from SleepQuality.Libraries.AuxiliaryFunction import createNewStatusList
from SleepQuality.Libraries.AuxiliaryFunction import changeExtesionALLGroup
from SleepQuality.Libraries.notProcessedFile import csvFile
"Good5Sample.csv"

elaboratedFiles=[]
elaboratedFiles = changeExtesionALLGroup(csvFile, "Good5Sample.csv")
windowToTest = [90, 75, 60]
minGroupDim = 0

workbook = xlsxwriter.Workbook('../../Archivio/filterAround90.xlsx')
worksheet = workbook.add_worksheet()

column=0;
for num in windowToTest:
  worksheet.write(0, column, num)
  column += 1

statusGroup = createNewStatusList(windowToTest)
row = 1;
for numFile in range(13):
  numAwakeGroups = []
  print(elaboratedFiles[numFile])
  data = pd.read_csv(elaboratedFiles[numFile], sep=",")

  statusLevel = 2
  awakeGroups= awakeIntoGroups(data, "status")

  statusPoints = numpy.copy(data.loc[data["status"] == 0].index)
  statusLevelPoints = ["status"] * statusPoints.size
  plt.scatter(statusPoints, statusLevelPoints, marker=".")
  column = 0
  for newStatus, windowDim in statusGroup.items():
    awakeGroups = awakeIntoGroups(data, newStatus)

    tmp = []
    print(awakeGroups)
    for i in range(len(awakeGroups)):
      if awakeGroups[i]>minGroupDim:
        tmp.append(awakeGroups[i])
    numAwakeGroups.append(len(tmp))
    worksheet.write_number(row, column, len(tmp))
    column +=1

    statusLevel += 2
    statusPoints = numpy.copy(data.loc[data[newStatus] == 0].index)
    statusLevelPoints = [newStatus] * statusPoints.size
    plt.scatter(statusPoints, statusLevelPoints, marker=".")

  plt.title(elaboratedFiles[numFile])
  plt.xlabel("Time")
  plt.show()
  row +=1

workbook.close()
