
import pandas as pd

def calculateNewStatus(data, row, window, awake_parameter):
  pos_row = data.index[data['id'] == row['id']].tolist()[0]
  actual_status = row['status']
  if(pos_row< window):
    return actual_status
  else:
    window_frame = data.loc[pos_row-window+1:pos_row]
    sum = 0;
    for status in window_frame['status']:
      sum = sum + status
    return sum/window

def countAwakeMoments(data, statusName,f):
  data_awake = data.loc[data[statusName] == 0]
  print(data_awake)
  count_awake_period = []
  countInstants= 1;
  previous_id = -1;
  for id in data_awake['id']:
    if(abs(id-previous_id)>2):
      count_awake_period.append(countInstants)
      countInstants = 1;
    else:
      countInstants = countInstants + 1
    previous_id = id
  f.write(str(count_awake_period))
  return len(count_awake_period)

csvFile = "../Archivio/2022_03_13_bedsensordata.csv"
data = pd.read_csv(csvFile, sep=",")
data = data.dropna(how="any", axis=0)

f = open("../analyse2022_03_13-Group-averageStatus.txt", "w")

f.write("file: " + csvFile)
data["newStatus120"]=data.apply(lambda row: calculateNewStatus(data, row, 120, 0.8), axis=1)
data["newStatus60"]=data.apply(lambda row: calculateNewStatus(data, row, 60, 0.8), axis=1)
data["newStatus30"]=data.apply(lambda row: calculateNewStatus(data, row, 30, 0.8), axis=1)
data["newStatus15"]=data.apply(lambda row: calculateNewStatus(data, row, 15, 0.8), axis=1)
data["newStatus10"]=data.apply(lambda row: calculateNewStatus(data, row, 10, 0.8), axis=1)
data["newStatus5"]=data.apply(lambda row: calculateNewStatus(data, row, 5, 0.8), axis=1)
f.write("\n")

f.write("Awake moments")
f.write("Status: Number of \"awake\" moments:"+ str(countAwakeMoments(data,"status",f))+"\n")
f.write("newStatus120: Number of \"awake\" moments:"+ str(countAwakeMoments(data,"newStatus120",f))+"\n")
f.write("newStatus60: Number of \"awake\" moments:"+ str(countAwakeMoments(data,"newStatus60",f))+"\n")
f.write("newStatus30: Number of \"awake\" moments:"+ str(countAwakeMoments(data,"newStatus30",f))+"\n")
f.write("newStatus15: Number of \"awake\" moments:"+ str(countAwakeMoments(data,"newStatus15",f))+"\n")
f.write("newStatus10: Number of \"awake\" moments:"+ str(countAwakeMoments(data,"newStatus10",f))+"\n")
f.write("newStatus5: Number of \"awake\" moments:"+ str(countAwakeMoments(data,"newStatus5",f))+"\n")
f.write("\n")

f.close()