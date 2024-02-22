n, k = map(int, input().split())

dp = [[0] * (201) for _ in range(201)]

for i in range(201):
    dp[1][i] = 1
    dp[i][1] = i

for i in range(2, 201):
    for j in range(2, 201):
        dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000000

print(dp[k][n])
