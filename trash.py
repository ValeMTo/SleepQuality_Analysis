
import pandas as pd

def reportLawStatusTimeStamp(data, row, windowDim, awake):
  print("row: ")
  print(row.name)
  print("\n")

csvFile1 = "../Archivio/Test/test1.csv"
csvFile2 = "../Archivio/Test/test2.csv"

data = pd.read_csv(csvFile1, sep=";")
tmp = pd.read_csv(csvFile2, sep=";", )
tmp = tmp.dropna(how="any", axis=0)
tmp = tmp.reset_index()
tmp['id'] = tmp.index
print(tmp)
#data["test"]=data.apply(lambda row: reportLawStatusTimeStamp(data, row, 3, 0.8), axis=1)

data = pd.concat([data, tmp], ignore_index=True)