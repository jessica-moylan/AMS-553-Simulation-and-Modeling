import math
# acceptance rejection threshold is k need to change
k = .0025
#copied and pasted these for now but can call once uploaded to github
FRAUD_MEAN = 140
FRAUD_STANDARD_DEVIATION = 15
FRAUD_PERCENT_BETWEEN_1_AND_4 = 0.2 # 0.113 from given data
FRAUD_PERCENT_NOT_BETWEEN_1_AND_4 = 0.1 #0.0245 from given data


dfPeople = pd.read_csv('people_data.csv')
dfTT = pd.read_csv('transaction_table.csv')
# x is going to be the row in the transaction table
def NPtest (x):
  person = dfTT.at[x, "customer_id"]
  mu_p = dfPeople.at[person - 1, "average_amount_per_transaction"]
  sd_p = dfPeople.at[person - 1, "standard_deviation_amount_per_transaction"]
  transaction = dfTT.at[x, "amount"]
  fraud_exp = -math.pow((math.log(transaction)-FRAUD_MEAN),2)/(2*(FRAUD_STANDARD_DEVIATION**2))
  person_exp = -((math.log(transaction)-mu_p)**2)/(2*(sd_p**2))
  fraud_Ln = math.log(1/(transaction*FRAUD_STANDARD_DEVIATION*math.sqrt(2*math.pi)))
  person_Ln = fraud_Ln = math.log(1/(transaction*sd_p*math.sqrt(2*math.pi)))
  LNK_result = fraud_Ln + fraud_exp - person_Ln - person_exp
  return LNK_result
for i in range(10):
  if NPtest(i) < math.log(k):
    print(NPtest(i))
