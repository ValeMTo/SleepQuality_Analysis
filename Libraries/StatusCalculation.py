
# Calculate the new status by average of the previous elements.
# The amount of prevoius element is defined by the window.
def statusAverage(data, row, window):
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

# Calculate the new status based on the previous element,
# following these rules:
# If awakeProbability > inBedProbability * awake_parameter then status = 0
# if it is false and the measured status was 0 then status id 1,
# otherwise the measured status is equal to the new status.
# The probability references to the probability of having X value in the status on the defined window.
def reportLawStatus(data, row,window, awake_parameter):
  posRow = row.name
  actual_status = row['status']
  if(posRow< window):
    window_frame = data.loc[0:posRow]
  else:
    window_frame = data.loc[posRow-window+1:posRow]
  empty_bed_probability = window_frame.loc[window_frame['status']==0].count().get('id')/window
  full_bed_probability = window_frame.loc[(window_frame['status']==1) | (window_frame['status']==2)].count().get('id')/window
  if(empty_bed_probability > awake_parameter*full_bed_probability):
    return 0
  elif actual_status == 0:
    return 1
  else:
    return actual_status

