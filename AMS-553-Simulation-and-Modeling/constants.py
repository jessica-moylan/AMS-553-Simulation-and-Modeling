import os

DATA_SEED = int(os.environ.get("DATA_SEED", 50))

QUEUE_SEED = int(os.environ.get("QUEUE_SEED", 42))
NUM_REVIEWERS = int(os.environ.get("NUM_REVIEWERS", 2))
MEAN_REVIEW_TIME = float(os.environ.get("MEAN_REVIEW_TIME", 10))  # minutes

NUM_CUSTOMERS = int(os.environ.get("NUM_CUSTOMERS", 5))
NUM_TRANSACTIONS = int(os.environ.get("NUM_TRANSACTIONS", 1000))
FRAUD_MEAN = float(os.environ.get("FRAUD_MEAN", 140))
FRAUD_STANDARD_DEVIATION = float(os.environ.get("FRAUD_SD", 15))
FRAUD_PERCENT_BETWEEN_1_AND_4 = float(os.environ.get("FRAUD_RATE_NIGHT", 0.2)) # 0.113 from given data
FRAUD_PERCENT_NOT_BETWEEN_1_AND_4 = float(os.environ.get("FRAUD_RATE_DAY", 0.1)) #0.0245 from given data
