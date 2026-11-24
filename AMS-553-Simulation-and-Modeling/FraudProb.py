import math
import pandas as pd
from constants import *

# acceptance rejection threshold 
k = .5

dfPeople = pd.read_csv('AMS-553-Simulation-and-Modeling/data/people_data.csv')
dfTT = pd.read_csv('AMS-553-Simulation-and-Modeling/data/transaction_table.csv')
dfTT['transaction_time']=pd.to_datetime(dfTT['transaction_time']).dt.hour

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
for i in range(1000):
  if NPtest(i) > k:
    if k < NPtest(i) < k+3:
      if 1 <= dfTT.at[i,'transaction_time'] <= 4: 
        if dfTT.at[i,'is_fraud']==1:
          accuracy += 1;
      else:
        if dfTT.at[i,'is_fraud']==0:
          accuracy += 1;
    elif  NPtest(i) > k+3:
      if dfTT.at[i,'is_fraud']==1:
        accuracy += 1;
  else:
    if dfTT.at[i,'is_fraud']==0:
      accuracy += 1;
print(accuracy/1000);

