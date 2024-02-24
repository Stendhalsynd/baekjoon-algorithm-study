import sys
input = sys.stdin.readline

N = int(input().rstrip()) # N : 정수 N

# memo = {} # memo[n] : 정수 N 을 세가지 연산을 적절히 사용해 1을 만드는데 걸리는 횟수
# memo[1] = 0
# memo[2] = 1
# memo[3] = 1
# memo[4] = 2
# memo[5] = 3
# memo[6] = 2

# def dp(n):
#   if n not in memo:
#     if n % 3 == 0 and n % 2 != 0:
#       memo[n] = min(dp(n // 3) + 1, dp(n - 1) + 1)
#     elif n % 2 == 0 and n % 3 != 0:
#       memo[n] = min(dp(n // 2) + 1, dp(n - 1) + 1)
#     elif n % 3 == 0 and n % 2 == 0:
#       memo[n] = min(dp(n // 2) + 1, dp(n // 3) + 1, dp(n - 1) + 1)
#     else:
#       memo[n] = dp(n - 1) + 1
#   return memo[n]
# print(dp(N))

'''
Top-down 방식 -> Recurssion Error 발생
top down 방식은 recursion 재귀로 구현되며 memo 를 채워나가는 것을 memoization 이라 한다.

bottom up 방식은 iteration 반복문을 통해 구현되며 memo 를 채워나가는 것을 tabulation 이라 한다.
'''

# Bottom-up 방식

memo = {}
memo[1] = 0

def dp(n):
  for i in range(1, n):
    memo[i + 1] = min(memo.get(i + 1, N), memo[i] + 1)
    memo[i * 2] = min(memo.get(i * 2 , N), memo.get(i * 2 - 1, N) + 1, memo[i] + 1)
    memo[i * 3] = min(memo.get(i * 3, N), memo.get(i * 3 - 1, N) + 1,  memo[i] + 1)
  return memo[n]

print(dp(N))