import sys
input = sys.stdin.readline

N = int(input()) # N : 돌의 개수

'''
n: 1 -> 상근
n: 2 -> 창영
n: 3 -> 상근
n: 4 -> 창영
n: 5 -> 상근
...
'''

# print("SK" if N % 2 == 1 else "CY")

'''
dp[n] : 게임 횟수
dp[1]: 1, 상근
dp[2]: 2, 창영
dp[3]: 1, 상근
dp[4]: 2, 창영
dp[5]: 3, 상근
...

dp[n] = min(dp[n -1] + 1, dp[n - 3] + 1)
'''

memo = {}
memo[1] = 1
memo[2] = 2
memo[3] = 1

def dp(n):
  if n not in memo:
    memo[n] = min(dp(n - 1) + 1, dp(n - 3) + 1)
  return memo[n]

print('SK' if dp(N) % 2 == 1 else 'CY')