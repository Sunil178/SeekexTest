from bucket_ballls import iterr_combinations

def getExtraBalls(all_balls, bucket_weight):
    total_balls_size = sum(all_balls)
    if total_balls_size > bucket_weight:
        max_balls = -1
        i = 1
        while i <= len(all_balls):
            combinations = list(iterr_combinations(all_balls, i))
            for combination in combinations:
                temp_balls_sum = sum(combination)
                if temp_balls_sum <= bucket_weight and temp_balls_sum > max_balls:
                    max_balls = temp_balls_sum
            i += 1
    print(max_balls)

balls = [2, 3, 3]
weight = 5
getExtraBalls(balls, weight)
