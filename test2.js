function max(a,b)
    {
        return (a > b) ? a : b;
    }
    
function printknapSack(W, val)
{
    wt = val
    n = val.length
    let i, w;
    let response = [];
    let K = new Array(n + 1);
    for( i=0;i<K.length;i++)
    {
        K[i]=new Array(W+1);
        for(let j=0;j<W+1;j++)
        {
            K[i][j]=0;
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
    for (i = n; i > 0 && res > 0; i--)
    {
        if (res == K[i - 1][w])
            continue;
        else {
            response.push(wt[i - 1] + " ");
            res = res - val[i - 1];
            w = w - wt[i - 1];
        }
    }
    return response
}
