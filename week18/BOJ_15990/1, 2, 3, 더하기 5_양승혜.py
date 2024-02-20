import sys
input = sys.stdin.readline

n = int(input())
dp = [[0, 0, 0] for _ in range(100001)]
divide = 10 ** 9 + 9 # 1000000009 표현(계속 쓰기 귀찮았습니다...^-^...)

dp[1] = [1, 0, 0]   # 1로 끝나는 경우 1개
dp[2] = [0, 1, 0]   # 2로 끝나는 경우 1개
dp[3] = [1, 1, 1]   # 1, 2, 3으로 끝나는 경우 각 1개씩

# 점화식
for i in range(4, 100001):
    dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % divide
    dp[i][1] = (dp[i - 2][0] + dp[i - 2][2]) % divide
    dp[i][2] = (dp[i - 3][0] + dp[i - 3][1]) % divide

for _ in range(n):
    num = int(input())
    print(sum(dp[num]) % divide)
