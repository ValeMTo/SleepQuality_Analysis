
import pandas as pd
from datetime import datetime

def calculateNewStatus(data, row, window, awake_parameter):
  pos_row = data.index[data['id'] == row['id']].tolist()[0]
  actual_status = row['status']
  if(pos_row< window):
    return actual_status
  else:
    window_frame = data.loc[pos_row-window:pos_row]
    empty_bed_probability = window_frame.loc[window_frame['status']==0].count().get('id')/window_frame.count().get('id')
    full_bed_probability = window_frame.loc[(window_frame['status']==1) | (window_frame['status']==2)].count().get('id')/window_frame.count().get('id')
    if(empty_bed_probability > awake_parameter*full_bed_probability):
      return 0
    elif actual_status == 0:
      return 1
    else:
      return actual_status

def calculateErrors(data, statusName):
  print(statusName)
  #Calcolo il numero di valori strani/errati
  count_hr_error = data.loc[data['hr'] < 30].count().get('id')
  count_hr_empty_bed = data.loc[(data['hr'] < 30) & (data[statusName] == 0)].count().get('id')
  count_hr_movement = data.loc[(data['hr'] < 30) & (data[statusName] == 2)].count().get('id')

  print("Percentuale di errori in hr:", (count_hr_error / data.count().get('id')) * 100, "%, ovvero", count_hr_error,
        "/", data.count().get('id'))
  if(count_hr_error != 0):
    print("Percentuale di errori in hr provocata dal movimento è di:", (count_hr_movement / count_hr_error) * 100, "%")
    print("Percentuale di errori in hr con letto vuoto è di:", (count_hr_empty_bed / count_hr_error) * 100, "%")

  count_b2b_error = data.loc[data['b2b'] > 2000].count().get('id')
  count_b2b_empty_bed = data.loc[(data['b2b'] > 2000) & (data[statusName] == 0)].count().get('id')
  count_b2b_movement = data.loc[(data['b2b'] < 2000) & (data[statusName] == 2)].count().get('id')

  print("Percentuale di errori in b2b:", (count_b2b_error / data.count().get('id')) * 100, "%, ovvero", count_b2b_error,
        "/", data.count().get('id'))
  if(count_b2b_error != 0):
    print("Percentuale di errori in b2b provocata dal movimento è di:", (count_b2b_movement / count_b2b_error) * 100, "%")
    print("Percentuale di errori in b2b con letto vuoto è di:", (count_b2b_empty_bed / count_b2b_error) * 100, "%")

  # Calcolo numero di periodi svegli -- RIVEDI

  data_awake = data.loc[data[statusName] == 0]
  count_awake_period = 0
  prior_row = -1
  for row in data_awake["id"]:
    if (prior_row != -1 and abs(row - prior_row) > 1):
      ##################################################################################################################
      #TROVARE METODO PER FARE LA DIFFERENZA FRA DUE TIMESTAMP
      ##################################################################################################################
      print(str(data.loc[data['id'] == row].get('time_packet')))
      d1 = datetime.strptime(str(data.loc[data['id'] == row].get('time_packet')), "%Y-%m-%d %H:%M:%S.%f")
      d2 = datetime.strptime(str(data.loc[data['id'] == row+1].get('time_packet')), "%Y-%m-%d %H:%M:%S.%f")
      if(d2-d1>6):
        count_awake_period = count_awake_period + 1
    prior_row = row

  f.write(statusName +": Numero di periodi \"svegli\":"+ str(count_awake_period)+"\n")


def calculateDifferenceColums(data, column1, column2):
  count_differences = data.loc[data[column1] != data[column2]].count().get('id')
  f.write("Differenza fra: " + column1 + " e "+ column2 + " è: "+ str((count_differences/data.count().get('id'))*100)+ "%\n")

csvFile = "one_night.csv"
data = pd.read_csv(csvFile, sep=";")
data = data.dropna(how="any", axis=0)
print(data.columns)

f = open("analyse5.txt", "w")

calculateErrors(data, "status")
data["newStatus120"]=data.apply(lambda row: calculateNewStatus(data, row, 120, 0.8), axis=1)
calculateErrors(data, "newStatus120")
data["newStatus60"]=data.apply(lambda row: calculateNewStatus(data, row, 60, 0.8), axis=1)
calculateErrors(data, "newStatus60")
data["newStatus30"]=data.apply(lambda row: calculateNewStatus(data, row, 30, 0.8), axis=1)
calculateErrors(data, "newStatus30")
data["newStatus15"]=data.apply(lambda row: calculateNewStatus(data, row, 15, 0.8), axis=1)
calculateErrors(data, "newStatus15")
data["newStatus10"]=data.apply(lambda row: calculateNewStatus(data, row, 10, 0.8), axis=1)
calculateErrors(data, "newStatus10")
data["newStatus5"]=data.apply(lambda row: calculateNewStatus(data, row, 5, 0.8), axis=1)
calculateErrors(data, "newStatus5")
f.write("\n")

calculateDifferenceColums(data, "newStatus120", "status")
calculateDifferenceColums(data, "newStatus60", "status")
calculateDifferenceColums(data, "newStatus30", "status")
calculateDifferenceColums(data, "newStatus15", "status")
calculateDifferenceColums(data, "newStatus10", "status")
calculateDifferenceColums(data, "newStatus5", "status")
f.write("\n")

"""
calculateDifferenceColums(data, "newStatus120", "newStatus60")
calculateDifferenceColums(data, "newStatus120", "newStatus30")
calculateDifferenceColums(data, "newStatus120", "newStatus15")
calculateDifferenceColums(data, "newStatus120", "newStatus10")
calculateDifferenceColums(data, "newStatus120", "newStatus5")
f.write("\n")

calculateDifferenceColums(data, "newStatus60", "newStatus30")
calculateDifferenceColums(data, "newStatus60", "newStatus15")
calculateDifferenceColums(data, "newStatus60", "newStatus10")
calculateDifferenceColums(data, "newStatus60", "newStatus5")
f.write("\n")

calculateDifferenceColums(data, "newStatus30", "newStatus15")
calculateDifferenceColums(data, "newStatus30", "newStatus10")
calculateDifferenceColums(data, "newStatus30", "newStatus5")
f.write("\n")

calculateDifferenceColums(data, "newStatus15", "newStatus10")
calculateDifferenceColums(data, "newStatus15", "newStatus5")
f.write("\n")

calculateDifferenceColums(data, "newStatus10", "newStatus5")
f.write("\n")
"""
f.close()