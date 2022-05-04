
def calculateDifferenceColumns(data, column1, column2, f):
  count_differences = data.loc[data[column1] != data[column2]].count().get('id')
  f.write("Difference between: " + column1 + " and "+ column2 + " is: "+ str((count_differences/data.count().get('id'))*100)+ "%\n")

def createNewStatusList(list):
  newStatusList = {}
  for num in list:
    newStatusList["newStatus" + str(num)] = num
  return newStatusList

def createNewStatusAwakeList(list):
  newStatusList = {}
  for num in list:
    newStatusList["newStatus_" + str(num)] = num
  return newStatusList

def createNewStatusAwakeFiveList(list):
  newStatusList = {}
  for num in list:
    newStatusList["newStatus_" + str(num*5) + "_" + str(num)] = num
  return newStatusList

def createNewStatusAwakeRange(window, listAwake):
  newStatusList = {}
  for num in listAwake:
    newStatusList["newStatus_" + str(window) + "_" + str(num)] = num
  return newStatusList

def identifyMedian(column, window):
  output=[]
  num=0
  while num < column.size/window:
    median = int(calculateMedian(column[num*window:(num+1)*window+window]))
    output.append(median)
    num +=1

  return output

def calculateMedian(list):
  count=0
  for num in list:
    if num == 0:
      count += 1;

  if count > list.size/2:
    return 0
  return 1

def changeExtension(file, extensionName):
  file = file[:-4]
  file = file + extensionName
  return file

def changeExtesionALLGroup(files, extesionName):
  files2 = []
  for file in files:
    files2.append(changeExtension(file, extesionName))
  return files2