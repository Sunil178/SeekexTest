from copy import deepcopy

def printknapSack(W, val):
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

def getExcludeBalls(all_balls, include_balls):
    res_balls = deepcopy(all_balls)
    for all_ball in all_balls:
        if all_ball in include_balls:
            include_balls.remove(all_ball)
            res_balls.remove(all_ball)
    return res_balls

val = [ 8, 2, 2, 2, 3 ]
W = 5

balls = printknapSack(W, val)
print(balls)
res = getExcludeBalls(val, balls)
print(res)