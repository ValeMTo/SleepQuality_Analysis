
from datetime import datetime

# Divides into groups the awake moments.
# Count all zeros in each group and put the result into an array.
# All groups are considered only if there are at least two elements.
# Write on the file the array and return the length of the array,
# without counting cells with a number under 2 inside.
def awakeIntoGroups(data, statusName,f):
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