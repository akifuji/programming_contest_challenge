def knapsack(n, w, v, W):
    dp = [[0 for j in range(W+1)] for i in range(n+1)]
    for i in range(n):
        for j in range(W+1):
            if (j < w[i]):
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j], dp[i][j-w[i]]+v[i])
    print(dp[n][W])

n = 4
w = [2, 1, 3, 2]
v = [3, 2, 4, 2]
W = 5

knapsack(n, w, v, W)
