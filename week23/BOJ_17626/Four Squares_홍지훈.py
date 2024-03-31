n = int(input())
sq = [0 if i**0.5%1 else 1 for i in range(n+1)] # 제곱수는 1로 저장

mincount = 4
for i in range(int(n**0.5), 0, -1):
    if sq[n] : # n이 제곱수일 경우
        mincount=1
        break
    elif sq[n-i**2] : # 나머지가 제곱수일 경우
        mincount=2
        break
    else:
        for j in range(int((n-i**2)**0.5), 0, -1):
            if sq[(n-i**2)-j**2]: # 제곱수를 한번 더 뺀 나머지가 제곱수일 경우
                mincount=3
print(mincount)

"""
Python3 는 시간초과, PyPy3 만 통과하는 코드
import sys
input = sys.stdin.readline

n = int(input().rstrip())

def min_square_sum(n):
  squares = [i**2 for i in range(1, 224)]
  dp = [float('inf')] * (n + 1)
  dp[0] = 0
  for i in range(1, n + 1):
    for square in squares:
      if square <= i: # 현재 탐색하는 자연수 i보다 작거나 같은 제곱수
        dp[i] = min(dp[i], dp[i - square] + 1) # dp[i] : 현재 제곱수를 더했을 때 최소 개수
  return dp[n]

print(min_square_sum(n))
"""