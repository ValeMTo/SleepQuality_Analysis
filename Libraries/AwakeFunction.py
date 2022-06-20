
from datetime import timedelta

# Divides into groups the awake moments.
# Count all zeros in each group and put the result into an array.
# All groups are considered only if there are at least two elements.
# Write on the file the array and return the length of the array,
# without counting cells with a number under 2 inside.
def awakeIntoGroups(data, statusName):
  data_awake = data.loc[data[statusName] == 0]
  count_awake_period = []
  countInstants = 1
  previous_id = -1
  for id in data_awake['id']:
    if(abs(id-previous_id)>1):
      count_awake_period.append(countInstants)
      countInstants = 1;
    else:
      countInstants = countInstants + 1
    previous_id = id
  count_awake_period.append(countInstants)

  if(count_awake_period[0] ==1):
    count_awake_period=count_awake_period[1:]
  return count_awake_period

# Divides into groups the given array the awake moments.
# Save the first instant of each group and save the amount of time awake passed from that time.
# Everything is saved in time unit.
def awakeBeginningMoment(data):
  count_awake_begin = []
  previous_id = data[0]
  countInstants = 1;
  isFirst=True
  for id in data:
    if(isFirst):
      begin = id;
      isFirst=False

    if(abs(id-previous_id)>1):
      count_awake_begin.append([str(timedelta(seconds=int(begin))), "time awake:" + str(timedelta(seconds=int(countInstants)))])
      countInstants = 1;
      isFirst=True
    else:
      countInstants = countInstants + 1
    previous_id = id
  count_awake_begin.append([str(timedelta(seconds=int(begin))), "time awake:" + str(timedelta(seconds=int(countInstants)))])

  return count_awake_begin


