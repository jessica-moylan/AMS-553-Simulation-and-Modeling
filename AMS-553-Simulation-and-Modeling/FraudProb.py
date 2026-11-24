import math
import pandas as pd
from constants import *

# acceptance rejection threshold 
k = .5

dfPeople = pd.read_csv('AMS-553-Simulation-and-Modeling/data/people_data.csv')
dfTT = pd.read_csv('AMS-553-Simulation-and-Modeling/data/transaction_table.csv')
dfTT['hour'] = pd.to_datetime(dfTT['transaction_time']).dt.hour

# x is going to be the row in the transaction table
def NPtest (x):
  person = dfTT.at[x, "customer_id"]
  mu_p = dfPeople.at[person - 1, "average_amount_per_transaction"]
  sd_p = dfPeople.at[person - 1, "standard_deviation_amount_per_transaction"]
  transaction = dfTT.at[x, "amount"]
  personPDF = (1/(math.sqrt(2*math.pi)*sd_p))*math.exp(-((transaction - mu_p)**2)/(2*(sd_p**2)))
  fraudPDF = (1/(math.sqrt(2*math.pi)*FRAUD_STANDARD_DEVIATION))*math.exp(-((transaction - FRAUD_MEAN)**2)/(2*(FRAUD_STANDARD_DEVIATION**2)))
  return(fraudPDF/personPDF)

accuracy = 0;
def is_flagged(i):
  ratio = NPtest(i)
  if ratio > k + 3:
    return 1
  if ratio > k and 1 <= dfTT.at[i, 'hour'] <= 4:
    return 1
  return 0

#print(accuracy/1000);
dfTT['flagged'] = [is_flagged(i) for i in range(len(dfTT))]
dfTT.to_csv('AMS-553-Simulation-and-Modeling/data/transaction_table_flagged.csv', index=False)

accuracy = (dfTT['flagged'] == dfTT['is_fraud']).mean()
print(accuracy)
