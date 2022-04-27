import pandas as pd
import numpy
import matplotlib.pyplot as plt
import xlsxwriter
from SleepQuality.AwakeFunction import awakeIntoGroups
from SleepQuality.AuxiliaryFunction import createNewStatusAwakeFiveList

csvFile = []
csvFile.append("..\Archivio\EachSecond\\bed_raw_2022-03-24_60-F1-89-29-82-44_complex5Sample.csv")
csvFile.append("..\Archivio\EachSecond\\bed_raw_2022-03-25_60-F1-89-29-82-44_complex5Sample.csv")
csvFile.append("..\Archivio\EachSecond\\bed_raw_2022-03-26_60-F1-89-29-82-44_complex5Sample.csv")
csvFile.append("..\Archivio\EachSecond\\bed_raw_2022-03-27_60-F1-89-29-82-44_complex5Sample.csv")
csvFile.append("..\Archivio\EachSecond\\bed_raw_2022-03-28_60-F1-89-29-82-44_complex5Sample.csv")

csvFile.append("..\Archivio\EachSecond2\\bed_raw_2022-03-29_60-F1-89-29-82-44_complex5Sample.csv")
csvFile.append("..\Archivio\EachSecond2\\bed_raw_2022-03-30_60-F1-89-29-82-44_complex5Sample.csv")
csvFile.append("..\Archivio\EachSecond2\\bed_raw_2022-03-31_60-F1-89-29-82-44_complex5Sample.csv")
csvFile.append("..\Archivio\EachSecond2\\bed_raw_2022-04-01_60-F1-89-29-82-44_complex5Sample.csv")

csvFile.append("..\Archivio\EachSecond3\\bed_raw_2022-04-01_60-F1-89-29-82-44_complex5Sample.csv")
csvFile.append("..\Archivio\EachSecond3\\bed_raw_2022-04-02_60-F1-89-29-82-44_complex5Sample.csv")
csvFile.append("..\Archivio\EachSecond3\\bed_raw_2022-04-03_60-F1-89-29-82-44_complex5Sample.csv")
csvFile.append("..\Archivio\EachSecond3\\bed_raw_2022-04-04_60-F1-89-29-82-44_complex5Sample.csv")
csvFile.append("..\Archivio\EachSecond3\\bed_raw_2022-04-05_60-F1-89-29-82-44_complex5Sample.csv")

awakeToTest = [0.6, 0.7, 0.8, 0.9, 1]

windowToTest = [150, 120, 100, 90, 60]

workbook = xlsxwriter.Workbook('..\Archivio\\general.xlsx')
worksheet = workbook.add_worksheet()

column=0
for num in windowToTest:
  for awakeParameter in awakeToTest:
      worksheet.write(0, column, str(num)+"_"+str(awakeParameter))
      column += 1

for i in range(len(windowToTest)):
  windowToTest[i] = int(windowToTest[i]/5)

statusGroup = createNewStatusAwakeFiveList(windowToTest)

numAwakeGroups=[]
row=1
for numFile in range(3):
  print(csvFile[numFile])
  data = pd.read_csv(csvFile[numFile], sep=",")

  statusLevel = 2
  awakeGroups= awakeIntoGroups(data, "status")

  statusPoints = numpy.copy(data.loc[data["status"] == 0].index)
  statusLevelPoints = ["status"] * statusPoints.size
  plt.scatter(statusPoints, statusLevelPoints, marker=".")
  column = 0;
  for newStatus, windowDim in statusGroup.items():
    for awakeValue in awakeToTest:
      awakeGroups = awakeIntoGroups(data, newStatus+"_"+str(awakeValue))

      tmp = []
      for i in range(len(awakeGroups)):
        if awakeGroups[i] > 0:
          tmp.append(awakeGroups[i])
      numAwakeGroups.append(len(tmp))
      worksheet.write_number(row, column, len(tmp))
      column += 1

      statusLevel += 2
      statusPoints = numpy.copy(data.loc[data[newStatus+"_"+str(awakeValue)] == 0].index)
      statusLevelPoints = [newStatus+"_"+str(awakeValue)] * statusPoints.size
      plt.scatter(statusPoints, statusLevelPoints, marker=".")

  #plt.title(csvFile[numFile])
  #plt.xlabel("Time")
  #plt.show()
  row+=1

workbook.close()


