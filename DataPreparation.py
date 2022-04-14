
import pandas as pd
from SleepQuality.StatusCalculation import reportLawStatus
from SleepQuality.AuxiliaryFunction import createNewStatusList

def outputFileName(file):
  file = file[:-4]
  file = file + "_elaborated90.csv"
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

windowToTest = [240, 180, 150, 120, 100, 90, 60, 45, 30, 20, 15, 10, 5]
statusGroup = createNewStatusList(windowToTest)

for numFile in range(10,14):
  print("From:", csvFile[numFile])
  print("To: ", outputFileName(csvFile[numFile]))
  data = pd.read_csv(csvFile[numFile], sep=";")
  data = data.dropna(how="any", axis=0)
  data = data.reset_index()

  data = data[['time_packet', 'hr', 'status', 'b2b']]
  data['id'] = data.index

  for newStatus, windowDim in statusGroup.items():
    print("Elaborating", newStatus, "...")
    data[newStatus]=data.apply(lambda row: reportLawStatus(data, row, windowDim, 0.9), axis=1)

  data.to_csv(outputFileName(csvFile[numFile]), encoding='utf-8')

