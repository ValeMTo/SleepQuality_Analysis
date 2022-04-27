import pandas as pd
from SleepQuality.StatusCalculation import reportLawStatus
from SleepQuality.AuxiliaryFunction import createNewStatusAwakeFiveList

def outputFileName(file):
  file = file[:-4]
  file = file + "_complex5Sample.csv"
  return file

csvFile = []
csvFile.append("..\Archivio\EachSecond\\bed_raw_2022-03-24_60-F1-89-29-82-44.csv")
csvFile.append("..\Archivio\EachSecond\\bed_raw_2022-03-25_60-F1-89-29-82-44.csv")
csvFile.append("..\Archivio\EachSecond\\bed_raw_2022-03-26_60-F1-89-29-82-44.csv")
csvFile.append("..\Archivio\EachSecond\\bed_raw_2022-03-27_60-F1-89-29-82-44.csv")
csvFile.append("..\Archivio\EachSecond\\bed_raw_2022-03-28_60-F1-89-29-82-44.csv")

csvFile.append("..\Archivio\EachSecond2\\bed_raw_2022-03-29_60-F1-89-29-82-44.csv")
csvFile.append("..\Archivio\EachSecond2\\bed_raw_2022-03-30_60-F1-89-29-82-44.csv")
csvFile.append("..\Archivio\EachSecond2\\bed_raw_2022-03-31_60-F1-89-29-82-44.csv")
csvFile.append("..\Archivio\EachSecond2\\bed_raw_2022-04-01_60-F1-89-29-82-44.csv")

csvFile.append("..\Archivio\EachSecond3\\bed_raw_2022-04-01_60-F1-89-29-82-44.csv")
csvFile.append("..\Archivio\EachSecond3\\bed_raw_2022-04-02_60-F1-89-29-82-44.csv")
csvFile.append("..\Archivio\EachSecond3\\bed_raw_2022-04-03_60-F1-89-29-82-44.csv")
csvFile.append("..\Archivio\EachSecond3\\bed_raw_2022-04-04_60-F1-89-29-82-44.csv")
csvFile.append("..\Archivio\EachSecond3\\bed_raw_2022-04-05_60-F1-89-29-82-44.csv")

awakeToTest = [0.6, 0.7, 0.8, 0.9, 1]

windowToTest = [150, 120, 100, 90, 60]
for i in range(len(windowToTest)):
  windowToTest[i] = int(windowToTest[i]/5)

statusGroup = createNewStatusAwakeFiveList(windowToTest)


for numFile in range(14):
  print("From:", csvFile[numFile])
  print("To: ", outputFileName(csvFile[numFile]))
  data = pd.read_csv(csvFile[numFile], sep=";")
  data = data.dropna(how="any", axis=0)
  data = data.reset_index()

  data = data[['time_packet', 'hr', 'status', 'b2b']]
  data['id'] = data.index

  for newStatus, windowValue in statusGroup.items():
    for awakeValue in awakeToTest:
      print("Elaborating", newStatus + "_" + str(awakeValue), "...")
      data[newStatus+"_"+str(awakeValue)]=data.apply(lambda row: reportLawStatus(data, row, windowValue, awakeValue ), axis=1)

  data.to_csv(outputFileName(csvFile[numFile]), encoding='utf-8')

