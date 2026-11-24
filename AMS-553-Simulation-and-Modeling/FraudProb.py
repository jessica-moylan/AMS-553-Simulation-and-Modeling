import math
import pandas as pd
from constants import *
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
# acceptance rejection threshold 
#k = .5

#dfPeople = pd.read_csv('AMS-553-Simulation-and-Modeling/data/people_data.csv')
#dfTT = pd.read_csv('AMS-553-Simulation-and-Modeling/data/transaction_table.csv')
dfPeople = pd.read_csv(DATA_DIR / "people_data.csv")
dfTT = pd.read_csv(DATA_DIR / "transaction_table.csv")
dfTT['hour'] = pd.to_datetime(dfTT['transaction_time']).dt.hour

def lognormal_pdf(x, mean, sd):
  sigma2 = math.log(1 + sd**2 / mean**2)
  mu = math.log(mean) - sigma2 / 2
  return math.exp(-(math.log(x) - mu)**2 / (2 * sigma2)) / (x * math.sqrt(2 * math.pi * sigma2))

# x is going to be the row in the transaction table
def NPtest (x):
  person = dfTT.at[x, "customer_id"]
  mu_p = dfPeople.at[person - 1, "average_amount_per_transaction"]
  sd_p = dfPeople.at[person - 1, "standard_deviation_amount_per_transaction"]
  transaction = dfTT.at[x, "amount"]
  #personPDF = (1/(math.sqrt(2*math.pi)*sd_p))*math.exp(-((transaction - mu_p)**2)/(2*(sd_p**2)))
  #fraudPDF = (1/(math.sqrt(2*math.pi)*FRAUD_STANDARD_DEVIATION))*math.exp(-((transaction - FRAUD_MEAN)**2)/(2*(FRAUD_STANDARD_DEVIATION**2)))
  personPDF = lognormal_pdf(transaction, mu_p, sd_p)
  fraudPDF = lognormal_pdf(transaction, FRAUD_MEAN, FRAUD_STANDARD_DEVIATION)
  return(fraudPDF/personPDF)

#accuracy = 0;
def is_flagged(i, k=0.5):
  ratio = NPtest(i)
  if ratio > k + 3:
    return 1
  if ratio > k and 1 <= dfTT.at[i, 'hour'] <= 4:
    return 1
  return 0


if __name__ == "__main__":
  #print(accuracy/1000);
  dfTT['flagged'] = [is_flagged(i) for i in range(len(dfTT))]
  #dfTT.to_csv('AMS-553-Simulation-and-Modeling/data/transaction_table_flagged.csv', index=False)
  dfTT.to_csv(DATA_DIR / "transaction_table_flagged.csv", index=False)

  #accuracy = (dfTT['flagged'] == dfTT['is_fraud']).mean()
  #print(accuracy)

#  tp = ((dfTT['flagged'] == 1) & (dfTT['is_fraud'] == 1)).sum()
#  fp = ((dfTT['flagged'] == 1) & (dfTT['is_fraud'] == 0)).sum()
#  fn = ((dfTT['flagged'] == 0) & (dfTT['is_fraud'] == 1)).sum()
#  print(f"caught {tp}, false alarms {fp}, missed {fn}")
#  print(f"recall {tp / (tp + fn):.3f}, precision {tp / (tp + fp):.3f}")

  caught = (dfTT['flagged'] & dfTT['is_fraud']).sum()
  fp = dfTT['flagged'].sum() - caught
  fn = dfTT['is_fraud'].sum() - caught
  print("caught", caught, "| false alarms", fp, "| missed", fn)
  print("recall", caught / dfTT['is_fraud'].sum(), "| precision", caught / dfTT['flagged'].sum())