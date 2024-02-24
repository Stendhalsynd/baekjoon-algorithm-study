# DP - bottom up
n = int(input())
dp = [0] * (n + 1)

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i // 2] + 1, dp[i])
    if i % 3 == 0:
        dp[i] = min(dp[i // 3] + 1, dp[i])

print(dp[n]) 

# 재귀 - top down
n = int(input())

dp = {1 : 0}  # 1의 최솟값 : 0

def rec(n):
    if n in dp.keys():
        return dp[n]
    if n % 3 == 0 and n % 2 == 0:
        dp[n] = min(rec(n // 3) + 1, rec(n // 2) + 1)
    elif n % 3 == 0:
        dp[n] = min(rec(n // 3) + 1, rec(n - 1) + 1)
    elif n % 2 == 0:
        dp[n] = min(rec(n // 2) + 1, rec(n - 1) + 1)
    else:
        dp[n] = rec(n - 1) + 1
    return dp[n]

print(rec(n))
