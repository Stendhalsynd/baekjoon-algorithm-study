import sys
from itertools import permutations
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip()) # N : 질문 횟수

nums = [1,2,3,4,5,6,7,8,9]

def calc_strike(num1: str, target: str) -> int:
  count = 0
  for i in range(3):
    if num1[i] == target[i]:
      count += 1
  return count

def calc_ball(num1: str, target: str) -> int:
  count = 0
  for i in range(3):
    if num1[i] != target[i] and num1[i] in target:
      count += 1
  return count

target_list = deque([])
for _ in range(N): 
  ans, strike, ball = map(int, input().rstrip().split())
  if not target_list: # 아직 후보군을 정하지 못한 초기라면
    for tuple in list(permutations(nums, 3)): # 순열을 사용해 가능한 모든 후보군중 가능한 후보군을 선정합니다.
      num = ''.join(map(str, tuple))

      if calc_strike(str(ans), num) == strike and calc_ball(str(ans), num) == ball and num not in target_list: # 후보군중 스트라이크 수, 볼 수, 중복을 제외한 후보군으로 초기화합니다.
        target_list.append(num)
  else:
    temp = list(target_list)
    for tuple in target_list:
      num = ''.join(map(str, tuple))

      if calc_strike(str(ans), num) != strike or calc_ball(str(ans), num) != ball: # 두번째 질문부터 후보군중 조건을 만족하지 않는 후보를 제거합니다.
        temp.remove(num)
    target_list = deque(temp)

print(len(target_list))