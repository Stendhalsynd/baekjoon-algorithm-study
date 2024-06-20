import sys, itertools
input = sys.stdin.readline

N, L, R, X = map(int, input().rstrip().split()) # N: 문제의 수, L <= 문제 난이도의 합 <= R, 가장 어려운 문제 - 가장 쉬운 문제 난이도 차이 >= X
difficulty = list(map(int, input().rstrip().split()))
result = 0

for n in range(2, N + 1):
  cases = list(itertools.combinations(difficulty, n))

  for problems in cases:
    min_prob = min(problems)
    max_prob = max(problems)
    if R >= sum(problems) >= L and max_prob - min_prob >= X:
      result += 1

print(result)