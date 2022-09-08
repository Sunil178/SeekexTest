def knapSack(W, val):
    n = len(val)
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    # Build tаble K[][] in bоttоm uр mаnner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0  or  w == 0:
                K[i][w] = 0
            elif val[i-1] <= w:
                K[i][w] = max(val[i-1]
                        + K[i-1][w-val[i-1]],
                            K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
            print(K[i])
    return K[n][W]
    # return K
# Driver code
val = [2, 3, 3]
W = 5
print(knapSack(W, val))
