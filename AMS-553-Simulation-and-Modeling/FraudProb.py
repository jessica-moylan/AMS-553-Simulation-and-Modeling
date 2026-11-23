import math
import pandas as pd
from constants import *

# acceptance rejection threshold is k need to change
k = .5

dfPeople = pd.read_csv('AMS-553-Simulation-and-Modeling/data/people_data.csv')
dfTT = pd.read_csv('AMS-553-Simulation-and-Modeling/data/transaction_table.csv')
# x is going to be the row in the transaction table
def NPtest (x):
  person = dfTT.at[x, "customer_id"]
  mu_p = dfPeople.at[person - 1, "average_amount_per_transaction"]
  sd_p = dfPeople.at[person - 1, "standard_deviation_amount_per_transaction"]
  transaction = dfTT.at[x, "amount"]
  personPDF = (1/(math.sqrt(2*math.pi)*sd_p))*math.exp(-((transaction - mu_p)**2)/(2*(sd_p**2)))
  fraudPDF = (1/(math.sqrt(2*math.pi)*FRAUD_STANDARD_DEVIATION))*math.exp(-((transaction - FRAUD_MEAN)**2)/(2*(FRAUD_STANDARD_DEVIATION**2)))
  # fraud_exp = math.exp(-math.pow((math.log(transaction)-FRAUD_MEAN),2)/(2*(FRAUD_STANDARD_DEVIATION**2)))
  # person_exp = math.exp(-((math.log(transaction)-mu_p)**2)/(2*(sd_p**2)))
  # fraud_mult = 1/(transaction*FRAUD_STANDARD_DEVIATION*math.sqrt(2*math.pi))
  # person_mult = 1/(transaction*sd_p*math.sqrt(2*math.pi))
  #return (fraud_mult*fraud_exp)/(person_mult*person_exp)
  return(fraudPDF/personPDF)
for i in range(50):
  if NPtest(i) > k:
    print(i+1)
