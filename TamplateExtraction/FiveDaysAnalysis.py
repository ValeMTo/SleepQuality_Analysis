
from AwakeFunction import awakeIntoGroupsVoid
from StatusCalculation import reportLawStatus
from AuxiliaryFunction import calculateDifferenceColumns
from AuxiliaryFunction import createNewStatusList
import pandas as pd;

windows = [120, 90, 60, 30, 20, 15, 10, 5]

csvFile = []
csvFile.append("..\Archivio\EachSecond\\bed_raw_2022-03-24_60-F1-89-29-82-44.csv")
csvFile.append("..\Archivio\EachSecond\\bed_raw_2022-03-25_60-F1-89-29-82-44.csv")
csvFile.append("..\Archivio\EachSecond\\bed_raw_2022-03-26_60-F1-89-29-82-44.csv")
csvFile.append("..\Archivio\EachSecond\\bed_raw_2022-03-27_60-F1-89-29-82-44.csv")
csvFile.append("..\Archivio\EachSecond\\bed_raw_2022-03-28_60-F1-89-29-82-44.csv")

f = open("../../24-28March_Analysis2", "w")
timeFile = open("../../24-28MarchTiming2", "w")
f.write("Files:")
data = pd.read_csv(csvFile[0], sep=";")
data = data[['time_packet','hr', 'status', 'b2b']]
for fileName in csvFile[1:]:
  f.write(fileName + ";\n")
  tmp = pd.read_csv(fileName, sep=";")
  tmp = tmp[['time_packet','hr', 'status', 'b2b']]
  data = pd.concat([data, tmp], ignore_index=True)
data = data.dropna(how="any", axis=0)
data = data.reset_index()
data["id"] = data.index
#count_differences = calculateErrors(data, "status")
data = data[['id','time_packet','status']]

newStatusList = createNewStatusList(windows)
print("Beginning newStatus calculation...")
for newStatus, windowDim in newStatusList.items():
  print("Starting", newStatus, "...")
  data[newStatus]=data.apply(lambda row: reportLawStatus(data, row,windowDim, 0.8), axis=1)
f.write("\n")

awakeIntoGroupsVoid(data,"status", f, timeFile)
for newStatus in newStatusList:
  awakeIntoGroupsVoid(data, newStatus, f, timeFile)
f.write("\n")

for newStatus in newStatusList:
  calculateDifferenceColumns(data, "status", newStatus, f)
f.write("\n")
