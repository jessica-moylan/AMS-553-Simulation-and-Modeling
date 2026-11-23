from random_variate_generator import RandomVariateGenerator

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



if __name__ == "__main__":
    results = simulate_queue([0, 1, 2, 10], [5, 5, 5, 5], num_reviewers=1)
    for customer in results:
        print(customer)