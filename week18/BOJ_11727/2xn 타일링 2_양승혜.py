n = int(input())
divide = 10 ** 4 + 7 # 10007을 이렇게한번 표현해봤습니다!
dp = [0] * (n + 1)

dp[0], dp[1] = 1, 1

for i in range(2, n + 1):
    dp[i] = (dp[i - 1] + (dp[i - 2] * 2)) % divide # 점화식

print(dp[n])
