import sys
input = sys.stdin.readline

N = int(input().rstrip()) # N : 민규가 구매하려는 카드의 개수
P = [int(val) for val in input().rstrip().split()]

def max_payment(N, prices):
  dp = [0] * (N + 1)
  
  for i in range(1, N + 1):
    for j in range(1, i + 1):
      dp[i] = max(dp[i], dp[i - j] + prices[j - 1])
  
  return dp[N]

print(max_payment(N, P))