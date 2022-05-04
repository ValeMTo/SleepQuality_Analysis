
import matplotlib.pyplot as plt
import xlsxwriter
from SleepQuality.Libraries.ProcessedFiles import csvFile1, csvFile5, csvFile10
from SleepQuality.Libraries.PlotFunction import createGraphOf, createGraphOfStatus

workbook = xlsxwriter.Workbook('../../Archivio/compare10_5_1.xlsx')
worksheet = workbook.add_worksheet()


for numFile in range(4):
  print("Analysis", numFile)

  createGraphOfStatus(csvFile1[numFile])

  createGraphOf(90, csvFile1[numFile], 1)
  createGraphOf(75, csvFile5[numFile], 5)
  createGraphOf(50, csvFile10[numFile], 10)

  plt.xlabel("Time")
  plt.show()

workbook.close()
