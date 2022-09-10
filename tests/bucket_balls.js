function iterr_combinations(array, size) {

    function p(t, i) {
        if (t.length === size) {
            result.push(t);
            return;
        }
        if (i + 1 > array.length) {
            return;
        }
        p(t.concat(array[i]), i + 1);
        p(t, i + 1);
    }

    var result = [];
    p([], 0);
    return result;
}

function remove(array, element) {
    const index = array.indexOf(element);
    if (index > -1) {
      array.splice(index, 1);
    }
    return array;
}

function getExcludeBalls(all_balls, include_balls) {
    res_balls = structuredClone(all_balls)
    for (let x in all_balls) {
        if (include_balls.includes(all_balls[x])) {
			remove(include_balls, all_balls[x]);
			remove(res_balls, all_balls[x]);
		}
	}
    return res_balls
}

function max(a,b) {
	return (a > b) ? a : b;
}

function knapSack(W, val)
{
    wt = structuredClone(val)
    n = val.length
    let i, j, w;
    let response = [];
    let K = new Array(n + 1);
    for(i = 0; i < K.length; i++)
    {
        K[i] = new Array(W+1);
        for(j = 0; j < W + 1; j++)
        {
            K[i][j] = 0;
        }
    }
    for (i = 0; i <= n; i++) {
        for (w = 0; w <= W; w++) {
            if (i == 0 || w == 0)
                K[i][w] = 0;
            else if (wt[i - 1] <= w)
                K[i][w] = Math.max(val[i - 1] +
                    K[i - 1][w - wt[i - 1]],
                    K[i - 1][w]);
            else
                K[i][w] = K[i - 1][w];
        }
    }
    let res = K[n][W];
    w = W;
    for (i = n; i > 0; i--)
    {
        if (res <= 0)
            break;
        if (res == K[i - 1][w])
            continue;
        else {
            response.push(wt[i - 1]);
            res = res - val[i - 1];
            w = w - wt[i - 1];
        }
    }
    return response
}

function getLossAndBuckets(p_buckets) {
    let temp_balls = structuredClone(balls);
    var empty_spaces = 0;
    for (let x in p_buckets) {
        if (temp_balls.length > 0) {
            response = knapSack(p_buckets[x], temp_balls);
			bucket_utilization = response.reduce((pv, cv) => pv + cv, 0);
            empty_spaces += (p_buckets[x] - bucket_utilization);
            temp_balls = getExcludeBalls(temp_balls, response);
		}
	}
    return empty_spaces
}

buckets = {"A": 5, "B": 10, "C": 3}
balls = [2, 3, 5, 2]
total_ball_volumes = balls.reduce((pv, cv) => pv + cv, 0);
console.log("total_ball_volumes", total_ball_volumes);

minimum_loss_combinations = {'loss': Infinity, 'combination': null}
var min_boxused_count = Infinity
i = 1
while (i <= Object.values(buckets).length) {
    combinations = iterr_combinations(Object.values(buckets), i)
	for (let x in combinations) {
		sum_combination = combinations[x].reduce((pv, cv) => pv + cv, 0);
        if (sum_combination >= total_ball_volumes) {
			let loss = getLossAndBuckets(combinations[x])
            console.log("Main", combinations[x], loss)
            if (loss <= minimum_loss_combinations['loss']) {
                if (loss == minimum_loss_combinations['loss'] && min_boxused_count < combinations[x].length)
                    continue
                min_boxused_count = combinations[x].length
                minimum_loss_combinations['loss'] = loss;
                minimum_loss_combinations['combination'] = combinations[x];
			}
		}
	}
    i += 1
}

console.log(minimum_loss_combinations)


