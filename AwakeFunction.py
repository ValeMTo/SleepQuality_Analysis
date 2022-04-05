
from datetime import datetime

# Divides into groups the awake moments.
# Count all zeros in each group and put the result into an array.
# All groups are considered only if there are at least two elements.
# Write on the file the array and return the length of the array,
# without counting cells with a number under 2 inside.
def awakeIntoGroups(data, statusName,f):
  data_awake = data.loc[data[statusName] == 0]
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

# Divides into groups the awake moments.
# Count all zeros in each group and put the result into an array.
# All groups are considered only if there are at least two elements.
# Write on the file the array and return the length of the array,
# without counting cells with a number under 2 inside.
def awakeIntoGroupsVoid(data, statusName,f):
  data_awake = data.loc[data[statusName] == 0]
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
  f.write(len(count_awake_period),"\n")
  f.write(str(count_awake_period),"\n")

# Divides into groups the awake moments thanks to timestamp.
# Count all zeros in each group and put the result into an array.
# All groups are considered only if there are at least two elements.
# Write on the file the array and return the length of the array,
# without counting cells with a number under 2 inside.
def awakeIntoGroupsVoidTimeStamp(data, statusName,f):
  data_awake = data.loc[data[statusName] == 0]
  count_awake_period = []
  countInstants= 0
  previousId = data_awake['timestamp'][0]
  for id in data_awake['timestamp']:
    if(abs(id-previousId)>2 and previousId != 1800):
      count_awake_period.append(countInstants)
      countInstants = 1
    else:
      countInstants = countInstants + 1
    previousId = id
  f.write("Awake moments: " + len(count_awake_period)+ "\n")
  f.write(str(count_awake_period)+ "\n")

# The awake groups are counted as the difference of timestamps.
# When the difference is above 6, then is a awake moment.
# Returns the number of groups
def awakeTimestamps(data, statusName):
  dataAwake = data.loc[data[statusName] == 0]
  countAwakePeriod = 0
  priorRow = data.loc[0]
  for index, row in dataAwake.iterrows():
      d1 = datetime.strptime(str(row.get('time_packet')), "%Y-%m-%d %H:%M:%S.%f")
      d2 = datetime.strptime(str(priorRow.get('time_packet')), "%Y-%m-%d %H:%M:%S.%f")
      if(abs((d2-d1).seconds)>6):
        countAwakePeriod = countAwakePeriod + 1
      priorRow = row
  return countAwakePeriod