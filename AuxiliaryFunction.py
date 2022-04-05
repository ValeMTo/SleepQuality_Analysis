
def calculateDifferenceColumns(data, column1, column2, f):
  count_differences = data.loc[data[column1] != data[column2]].count().get('id')
  f.write("Difference between: " + column1 + " and "+ column2 + " is: "+ str((count_differences/data.count().get('id'))*100)+ "%\n")

def createNewStatusList(list):
  newStatusList = {}
  for num in list:
    newStatusList["newStatus" + str(num)] = num
  return newStatusList
