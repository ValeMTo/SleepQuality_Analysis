
import pandas as pd
from datetime import datetime

from StatusCalculation import reportLawStatus
from AwakeFunction import awakeTimestamps

#Count errors in the csv file
def calculateErrors(data, statusName):
  count_hr_error = data.loc[data['hr'] < 30].count().get('id')
  count_hr_empty_bed = data.loc[(data['hr'] < 30) & (data[statusName] == 0)].count().get('id')
  count_hr_movement = data.loc[(data['hr'] < 30) & (data[statusName] == 2)].count().get('id')

  print("hr errors:", (count_hr_error / data.count().get('id')) * 100, "%, that is", count_hr_error,
        "/", data.count().get('id'))
  if(count_hr_error != 0):
    print("hr errors, during a movement:", (count_hr_movement / count_hr_error) * 100, "%")
    print("hr errors with empty bed:", (count_hr_empty_bed / count_hr_error) * 100, "%")

  count_b2b_error = data.loc[data['b2b'] > 2000].count().get('id')
  count_b2b_empty_bed = data.loc[(data['b2b'] > 2000) & (data[statusName] == 0)].count().get('id')
  count_b2b_movement = data.loc[(data['b2b'] < 2000) & (data[statusName] == 2)].count().get('id')

  print("b2b errors:", (count_b2b_error / data.count().get('id')) * 100, "%, ovvero", count_b2b_error,
        "/", data.count().get('id'))
  if(count_b2b_error != 0):
    print("b2b errors during a movement:", (count_b2b_movement / count_b2b_error) * 100, "%")
    print("b2b errors with empty bed:", (count_b2b_empty_bed / count_b2b_error) * 100, "%")

def calculateDifferenceColums(data, column1, column2):
  count_differences = data.loc[data[column1] != data[column2]].count().get('id')
  f.write("Difference between: " + column1 + " and "+ column2 + " is: "+ str((count_differences/data.count().get('id'))*100)+ "%\n")


csvFile = "../Archivio/2022_03_14_bedsensordata.csv"
data = pd.read_csv(csvFile, sep=",")
data = data.dropna(how="any", axis=0)

count_awake = awakeTimestamps(data,"status")

f = open("../analyse2022_03_14.txt", "w")

f.write("file: " + csvFile)

count_differences = calculateErrors(data, "status")

data["newStatus120"]=data.apply(lambda row: reportLawStatus(data, row, 120, 0.8), axis=1)
data["newStatus60"]=data.apply(lambda row: reportLawStatus(data, row, 60, 0.8), axis=1)
data["newStatus30"]=data.apply(lambda row: reportLawStatus(data, row, 30, 0.8), axis=1)
data["newStatus15"]=data.apply(lambda row: reportLawStatus(data, row, 15, 0.8), axis=1)
data["newStatus10"]=data.apply(lambda row: reportLawStatus(data, row, 10, 0.8), axis=1)
data["newStatus5"]=data.apply(lambda row: reportLawStatus(data, row, 5, 0.8), axis=1)
f.write("\n")

f.write("Awake moments")
f.write("Status: Number of \"awake\" moments:"+ str(awakeTimestamps(data,"status"))+"\n")
f.write("newStatus120: Number of \"awake\" moments:"+ str(awakeTimestamps(data,"newStatus120"))+"\n")
f.write("newStatus60: Number of \"awake\" moments:"+ str(awakeTimestamps(data,"newStatus60"))+"\n")
f.write("newStatus30: Number of \"awake\" moments:"+ str(awakeTimestamps(data,"newStatus30"))+"\n")
f.write("newStatus15: Number of \"awake\" moments:"+ str(awakeTimestamps(data,"newStatus15"))+"\n")
f.write("newStatus10: Number of \"awake\" moments:"+ str(awakeTimestamps(data,"newStatus10"))+"\n")
f.write("newStatus5: Number of \"awake\" moments:"+ str(awakeTimestamps(data,"newStatus5"))+"\n")
f.write("\n")

calculateDifferenceColums(data, "newStatus120", "status")
calculateDifferenceColums(data, "newStatus60", "status")
calculateDifferenceColums(data, "newStatus30", "status")
calculateDifferenceColums(data, "newStatus15", "status")
calculateDifferenceColums(data, "newStatus10", "status")
calculateDifferenceColums(data, "newStatus5", "status")
f.write("\n")

f.close()
