import sys
input = sys.stdin.readline

n = int(input().rstrip())

memo = {}
memo[1] = 1
memo[2] = 3

def dp(n):
  if n not in memo:
    memo[n] = dp(n - 1) + 2 * dp(n - 2)
  return memo[n]

dp(n)
print(memo[n] % 10007)