from math import inf
from copy import deepcopy
def iterr_combinations(iterable, r):
    pool = list(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield list(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield list(pool[i] for i in indices)

def getExcludeBalls(all_balls, include_balls):
    res_balls = deepcopy(all_balls)
    for all_ball in all_balls:
        if all_ball in include_balls:
            include_balls.remove(all_ball)
            res_balls.remove(all_ball)
    return res_balls

def knapSack(W, val):
    wt = deepcopy(val)
    n = len(val)
    response = []
    K = [[0 for w in range(W + 1)]
            for i in range(n + 1)]
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1]
                  + K[i - 1][w - wt[i - 1]],
                               K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    res = K[n][W]
    # print(res)
    w = W
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == K[i - 1][w]:
            continue
        else:
            response.append(wt[i - 1])
            res = res - val[i - 1]
            w = w - wt[i - 1]
    return response

def getLossAndBuckets(p_buckets):
    global balls
    temp_balls = deepcopy(balls)
    empty_spaces = 0
    for p_bucket in p_buckets:
        if len(temp_balls) > 0:
            response = knapSack(p_bucket, temp_balls)
            # print("knapSack:", response)
            bucket_utilization = sum(response)
            empty_spaces += (p_bucket - bucket_utilization)
            temp_balls = getExcludeBalls(temp_balls, response)
    return empty_spaces

# buckets = {
# 	"A": 6,
# 	"B": 5,
# 	"C": 3,
# 	"D": 4,
# 	"E": 7
# }

buckets = {"A": 5, "B": 10, "C": 3}

"""
balls = {
	"PINK": {'value': 2.5, 'quantity': 0},
	"RED": {'value': 2, 'quantity': 0},
	"BLUE": {'value': 1, 'quantity': 0},
	"ORANGE": {'value': 0.8, 'quantity': 0},
	"GREEN": {'value': 0.5  , 'quantity': 0}
}

total_ball_volumes = 0;
total_ball_volumes += balls['PINK']['quantity'] * 3;
total_ball_volumes += balls['BLUE']['quantity'] * 5;
total_ball_volumes += balls['GREEN']['quantity'] * 3;
total_ball_volumes += balls['RED']['quantity'] * 1;
"""

# balls = [2, 2, 3, 5]
balls = [2, 3, 5, 2]
total_ball_volumes = sum(balls)

print("total_ball_volumes", total_ball_volumes);

minimum_loss_combinations = {'loss': inf, 'combination': None}
i = 1
while i <= len(buckets):
    combinations = list(iterr_combinations(buckets.values(), i))
    for combination in combinations:
        if sum(combination) >= total_ball_volumes:
            loss = getLossAndBuckets(combination)
            print(combination, loss)
            if loss < minimum_loss_combinations['loss']:
                minimum_loss_combinations['loss'] = loss
                minimum_loss_combinations['combination'] = combination
    i += 1

print(minimum_loss_combinations)
