import sys
input = sys.stdin.readline

sys.setrecursionlimit(10000000)

memo = {} # [a, b, c] 에서 a 는 마지막이 1 로 끝나는 경우의 수, b 는 2로 끝나는 경우의 수, c 는 3 으로 끝나는 경우의 수
memo[1] = [1, 0, 0]
memo[2] = [0, 1, 0]
memo[3] = [1, 1, 1]
memo[4] = [2, 0, 1]
memo[5] = [1, 2, 1]
memo[6] = [3, 3, 2]

'''
memo[1] 1, [1, 0, 0]
memo[2] 2, [0, 1, 0]
memo[3] 3 / 1 + 2 / 2 + 1, [1, 1, 1]
memo[4] 1 + 2 + 1 / 1 + 3 / 3 + 1, [2, 0, 1]
memo[5] 1 + 3 + 1 / 2 + 1 + 2 / 2 + 3 / 3 + 2, [1, 2, 1]
memo[6] 1 + 2 + 1 + 2 / 1 + 2 + 3 / 1 + 3 + 2 / 2 + 1 + 3 / 2 + 1 + 2 + 1 / 2 + 3 + 1 / 3 + 1 + 2 / 3 + 2 + 1, [3, 3, 2]
memo[7] 1 + 2 + 1 + 2 + 1 / 1 + 2 + 1 + 3 / 1 + 2 + 3 + 1 / 1 + 3 + 1 + 2 / 1 + 3 + 2 + 1 / 2 + 1 + 3 + 1 / 2 + 3 + 2 / 3 + 1 + 2 + 1 / 3 + 1 + 3, ?

memo[6] 을 계산해보면 아래와 같습니다.
memo[3] 1 + 2 | + 3
memo[3] 2 + 1 | + 3
memo[4] 1 + 2 + 1 | + 2
memo[4] 1 + 3 | + 2
memo[4] 3 + 1 | + 2
memo[5] 2 + 1 + 2 | + 1
memo[5] 2 + 3 | + 1
memo[5] 3 + 2 | + 1

죽, dp 를 적용한 점화식을 구할 때 memo[n] 을 구할 경우
memo[n - 3] 의 경우 -> 마지막에 3을 추가해야 할 때 : [a, b, c] 라면 memo[n - 3] 에서 a, b 에 3을 더할 경우가 유효
memo[n - 2] 의 경우 -> 마지막에 2를 추가해야 할 때 : [a, b, c] 라면 memo[n - 2] 에서 a, c 에 2을 더할 경우가 유효
memo[n - 1] 의 경우 -> 마지막에 1을 추가해야 할 때 : [a, b, c] 라면 memo[n - 1] 에서 b, c 에 1을 더할 경우가 유효
'''

def dp(n):
  global memo

  if n <= 0:
    return [0, 0, 0]

  if n not in memo:
    prev = dp(n - 1), dp(n - 2), dp(n - 3)
    memo[n] = [(prev[0][1] + prev[0][2]) % 1000000009, (prev[1][0] + prev[1][2]) % 1000000009, (prev[2][0] + prev[2][1]) % 1000000009]

  return memo[n]

result = []

T = int(input().rstrip()) # T: 테스트 케이스 수
for _ in range(T):
  n = int(input().rstrip())
  result.append(sum(dp(n)) % 1000000009)

[print(val) for val in result]