
from SleepQuality.Libraries.StatusCalculation import reportLawStatus
from SleepQuality.Libraries.notProcessedFile import csvFile
import timeit
import pandas as pd

f = open("../../24-28March_Analysis", "w")
timeFile = open("../../24-28MarchTiming", "w")
f.write("Files:")
data = pd.read_csv(csvFile[0], sep=";")
data = data[['time_packet','hr', 'status', 'b2b']]
for fileName in csvFile:
  f.write(fileName + ";\n")
  tmp = pd.read_csv(fileName, sep=";")
  tmp = tmp[['time_packet','hr', 'status', 'b2b']]
  data = pd.concat([data, tmp], ignore_index=True)
data = data.dropna(how="any", axis=0)
data = data.reset_index()
data["id"] = data.index
#count_differences = calculateErrors(data, "status")
data = data[['id','time_packet','status']]

row = data.iloc[560]
print("window: 120")
print(timeit.timeit(lambda: reportLawStatus(data, row, 120, 0.8), number=10000)/10000)
