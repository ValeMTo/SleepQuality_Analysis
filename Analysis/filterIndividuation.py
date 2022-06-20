
# The goal is to find the best filter window.
# When can we be sure of the awake action?

import pandas as pd
import xlsxwriter
from matplotlib import pyplot as plt

from SleepQuality.Libraries.AwakeFunction import awakeIntoGroups
from SleepQuality.Libraries.AuxiliaryFunction import createNewStatusList
from SleepQuality.Libraries.AuxiliaryFunction import changeExtesionALLGroup
from SleepQuality.Libraries.notProcessedFile import csvFile4
from SleepQuality.Libraries.PlotFunction import createGraphOf

csvFile = csvFile4

elaboratedFiles=[]
elaboratedFiles = changeExtesionALLGroup(csvFile, "_Good5Sample.csv")
windowToTest = [150, 120, 100, 90, 60]
medianWindow = 5
minGroupDim = 1 #included

workbook = xlsxwriter.Workbook('../../Archivio/filter5.xlsx')
worksheet = workbook.add_worksheet()

column=0;
for num in windowToTest:
  worksheet.write(0, column, num)
  column += 1

statusGroup = createNewStatusList(windowToTest)
row = 1;
for numFile in range(len(csvFile)):
  numAwakeGroups = []
  print(elaboratedFiles[numFile])
  data = pd.read_csv(elaboratedFiles[numFile], sep=",")

  statusLevel = 2
  awakeGroups= awakeIntoGroups(data, "status")

  createGraphOf('status', data, medianWindow)

  column = 0
  for newStatus, windowDim in statusGroup.items():
    print(newStatus)
    awakeGroups = awakeIntoGroups(data, newStatus)

    tmp = []
    print(awakeGroups)
    for i in range(len(awakeGroups)):
      if awakeGroups[i]>=minGroupDim:
        tmp.append(awakeGroups[i])
    numAwakeGroups.append(len(tmp))
    worksheet.write_number(row, column, len(tmp))
    column +=1

    createGraphOf(newStatus, data, medianWindow)

  #plt.title(elaboratedFiles[numFile])
  #plt.xlabel("Time")
  #plt.show()
  row +=1

workbook.close()
