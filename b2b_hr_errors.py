
import pandas as pd

csvFile = "one_night.csv"
data = pd.read_csv(csvFile, sep=";")
data = data.dropna(how="any", axis=0)
print(data.columns)

count_hr_b2b_correct = data.loc[(data['hr'] > 30) & (data['b2b']<2000)].count().get('id')
count_hr_b2bFalse = data.loc[(data['hr'] > 30) & (data['b2b']>2000)].count().get('id')
count_b2b_hrFalse = data.loc[(data['hr'] < 30) & (data['b2b']<2000)].count().get('id')

count = data.count().get('id')

print("Correct data:", (count_hr_b2b_correct/count)*100, "%" )
print("False b2b data:", (count_hr_b2bFalse/count)*100, "%" )
print("False hr data:", (count_b2b_hrFalse/count)*100, "%" )