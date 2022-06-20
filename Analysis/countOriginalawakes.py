
import pandas as pd
from SleepQuality.Libraries.AwakeFunction import awakeIntoGroups
from SleepQuality.Libraries.notProcessedFile import allCsvFiles

csvFile = allCsvFiles

numGroups = 0
for numFile in range(len(csvFile)):
  #print(csvFile[numFile])

  beginData = pd.read_csv(csvFile[numFile], sep=";")
  beginData = beginData.dropna(how="any", axis=0)
  beginData = beginData.reset_index()

  data = pd.DataFrame()
  data['id'] = beginData.index
  data['status'] = beginData['status']
  awakeGroups= awakeIntoGroups(data, "status")

  numGroups += len(awakeGroups)

print("Average number of awakes: ", numGroups/len(csvFile))
