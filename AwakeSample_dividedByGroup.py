
import pandas as pd

from StatusCalculation import statusAverage
from AwakeFunction import awakeIntoGroups

csvFile = "../Archivio/2022_03_13_bedsensordata.csv"
data = pd.read_csv(csvFile, sep=",")
data = data.dropna(how="any", axis=0)

f = open("../analyse2022_03_13-Group-averageStatus.txt", "w")

f.write("file: " + csvFile)
data["newStatus120"]=data.apply(lambda row: statusAverage(data, row, 120, 0.8), axis=1)
data["newStatus60"]=data.apply(lambda row: statusAverage(data, row, 60, 0.8), axis=1)
data["newStatus30"]=data.apply(lambda row: statusAverage(data, row, 30, 0.8), axis=1)
data["newStatus15"]=data.apply(lambda row: statusAverage(data, row, 15, 0.8), axis=1)
data["newStatus10"]=data.apply(lambda row: statusAverage(data, row, 10, 0.8), axis=1)
data["newStatus5"]=data.apply(lambda row: statusAverage(data, row, 5, 0.8), axis=1)
f.write("\n")

f.write("Awake moments")
f.write("Status: Number of \"awake\" moments:"+ str(awakeIntoGroups(data,"status",f))+"\n")
f.write("newStatus120: Number of \"awake\" moments:"+ str(awakeIntoGroups(data,"newStatus120",f))+"\n")
f.write("newStatus60: Number of \"awake\" moments:"+ str(awakeIntoGroups(data,"newStatus60",f))+"\n")
f.write("newStatus30: Number of \"awake\" moments:"+ str(awakeIntoGroups(data,"newStatus30",f))+"\n")
f.write("newStatus15: Number of \"awake\" moments:"+ str(awakeIntoGroups(data,"newStatus15",f))+"\n")
f.write("newStatus10: Number of \"awake\" moments:"+ str(awakeIntoGroups(data,"newStatus10",f))+"\n")
f.write("newStatus5: Number of \"awake\" moments:"+ str(awakeIntoGroups(data,"newStatus5",f))+"\n")
f.write("\n")

f.close()