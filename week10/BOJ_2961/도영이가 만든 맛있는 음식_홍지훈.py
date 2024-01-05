import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input()) # N : 재료의 개수

# 룰 
# 신맛 : 재료 신맛의 곱, 쓴맛 : 재료 쓴맛의 합
# 목표 : 신맛과 쓴맛의 차이를 작게 만들자
# 재료는 적어도 하나

sour_list = [0] * N
bitter_list = [0] * N
nums = [i for i in range(N)]
min_diff = 1e9

for i in range(N):
  S, B = map(int, input().rstrip().split()) # S: 신맛, B: 쓴맛
  sour_list[i] = S
  bitter_list[i] = B

for i in range(1, N + 1):
  data = list(combinations(nums, i))
  for choice in data:
    mul_s = 1
    sum_b = 0
    for index in list(choice):
      mul_s *= sour_list[index]
      sum_b += bitter_list[index]
    if abs(mul_s - sum_b) < min_diff:
      min_diff = abs(mul_s - sum_b)

print(min_diff)