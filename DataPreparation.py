
import pandas as pd
from SleepQuality.StatusCalculation import reportLawStatus
from SleepQuality.AuxiliaryFunction import createNewStatusList

def outputFileName(file):
  file = file[:-4]
  file = file + "_elaborated.csv"
  return file

csvFile = []
csvFile.append("..\Archivio\EachSecond\\bed_raw_2022-03-24_60-F1-89-29-82-44.csv")
csvFile.append("..\Archivio\EachSecond\\bed_raw_2022-03-25_60-F1-89-29-82-44.csv")
csvFile.append("..\Archivio\EachSecond\\bed_raw_2022-03-26_60-F1-89-29-82-44.csv")
csvFile.append("..\Archivio\EachSecond\\bed_raw_2022-03-27_60-F1-89-29-82-44.csv")
csvFile.append("..\Archivio\EachSecond\\bed_raw_2022-03-28_60-F1-89-29-82-44.csv")

windowToTest = [120, 90, 60, 30, 20, 15, 10, 5]
statusGroup = createNewStatusList(windowToTest)

for numFile in range(5):
  print("From:", csvFile[numFile])
  print("To: ", outputFileName(csvFile[numFile]))
  data = pd.read_csv(csvFile[numFile], sep=";")
  data = data.dropna(how="any", axis=0)
  data = data.reset_index()

  data = data[['time_packet', 'hr', 'status', 'b2b']]
  data['id'] = data.index

  for newStatus, windowDim in statusGroup.items():
    print("Elaborating", newStatus, "...")
    data[newStatus]=data.apply(lambda row: reportLawStatus(data, row, windowDim, 0.8), axis=1)

  data.to_csv(outputFileName(csvFile[numFile]), encoding='utf-8')

