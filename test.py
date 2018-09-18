value, weight, amount
n = len(value)
dp = [[0 for i in range(amount + 1)] for j in range(n)]
for i in range(n):
    dp[i][0] = 0
for j in range(1, n):
    dp[0][j] = j // weight[0] * value[0]

for j in range(1, amount + 1):
    for i in range(1, n):
        if weight[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-weight[i]] + value[i])