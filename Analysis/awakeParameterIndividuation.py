import pandas as pd
import numpy
import matplotlib.pyplot as plt
import xlsxwriter
from SleepQuality.Libraries.AwakeFunction import awakeIntoGroups
from SleepQuality.Libraries.AuxiliaryFunction import createNewStatusAwakeRange
from SleepQuality.Libraries.AuxiliaryFunction import changeExtesionALLGroup
from SleepQuality.Libraries.notProcessedFile import allCsvFiles

csvFile = allCsvFiles

elaboratedFiles=[]
elaboratedFiles = changeExtesionALLGroup(csvFile, "_awakeRange7_70.csv" )

workbook = xlsxwriter.Workbook('../../Archivio/previousAwake.xlsx')
worksheet = workbook.add_worksheet()

awakeToTest = [0.8, 0.85, 0.9, 0.95, 1]
minGroupDim=1

statusGroup = createNewStatusAwakeRange(70, awakeToTest)
column=0;
for status in statusGroup:
  worksheet.write(0, column, status)
  column += 1

numAwakeGroups=[]
row = 1
for numFile in range(len(elaboratedFiles)):
  print(elaboratedFiles[numFile])
  data = pd.read_csv(elaboratedFiles[numFile], sep=",")

  statusLevel = 2
  awakeGroups= awakeIntoGroups(data, "status")

  statusPoints = numpy.copy(data.loc[data["status"] == 0].index)
  statusLevelPoints = ["status"] * statusPoints.size
  plt.scatter(statusPoints, statusLevelPoints, marker=".")
  column=0
  for newStatus, windowDim in statusGroup.items():
    awakeGroups = awakeIntoGroups(data, newStatus)

    tmp = []
    for i in range(len(awakeGroups)):
      if awakeGroups[i] > minGroupDim:
        tmp.append(awakeGroups[i])
    numAwakeGroups.append(len(tmp))
    worksheet.write_number(row, column, len(tmp))
    column += 1

    statusLevel += 2
    statusPoints = numpy.copy(data.loc[data[newStatus] == 0].index)
    statusLevelPoints = [newStatus] * statusPoints.size
    plt.scatter(statusPoints, statusLevelPoints, marker=".")

  #plt.title(elaboratedFiles[numFile])
  #plt.xlabel("Time")
  #plt.show()
  row +=1

workbook.close()