from random_variate_generator import RandomVariateGenerator
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DATA_DIR = Path(__file__).parent / "data"

def simulate_queue(arrival_times, review_times, num_reviewers):
    reviewers = [0] * num_reviewers
    results = []
    for arrival, review_time in zip(arrival_times, review_times):
        soonest = min(reviewers)
        free_reviewer = reviewers.index(soonest)
        
        start = max(arrival, reviewers[free_reviewer])
        finish = start + review_time
        
        reviewers[free_reviewer] = finish
        results.append({"arrival": arrival, 
                        "reviewer": free_reviewer, 
                        "start": start, 
                        "finish": finish, 
                        "wait": start-arrival})
    return results

def results_summary(results, num_reviewers):
    """
    Avg wait time
    Avg time in system (W)
    lambda
    Utilization
    Time avg number in system (L)
    Time-avg queue length (Lq) """
    if not results:
        return {"avg_wait": 0, "W": 0, "lambda": 0, "utilization": 0, "L": 0, "Lq": 0}
    waits = [customer["wait"] for customer in results]
    times_in_system = [customer["finish"] - customer["arrival"] for customer in results]
    review_times = [customer["finish"] - customer["start"] for customer in results]
    end_time = max([customer["finish"] for customer in results])
    n = len(results)

    # Avg wait time
    avg_wait = sum(waits) / n
    # Avg time in system (W)
    W = sum(times_in_system) / n
    # lambda
    lam = n / end_time
    utilization = sum(review_times) / (num_reviewers * end_time)
    # Time avg number in system (L)
    L = sum(times_in_system) / end_time
    # Time-avg queue length (Lq)
    Lq = sum(waits) / end_time

    return {"avg_wait": avg_wait, "W": W, "lambda": lam, "utilization": utilization, "L": L, "Lq": Lq}

if __name__ == "__main__":
    num_reviewers=2
    #results = simulate_queue([0, 1, 2, 10], [5, 5, 5, 5], num_reviewers=1)
    
    # random test
    #urv = RandomVariateGenerator(42)
    #arrivals = [i * 3 for i in range(20)]
    #review_times = [urv.exponential(rate=1/10) for _ in arrivals]
    #results = simulate_queue(arrivals, review_times, num_reviewers=1)
    
    results = simulate_queue([0, 1, 2, 10], [5, 5, 5, 5], num_reviewers)
    print(results_summary(results, num_reviewers))

    for customer in results:
        print(customer)