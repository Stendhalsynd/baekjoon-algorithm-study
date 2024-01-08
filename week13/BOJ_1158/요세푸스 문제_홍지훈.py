import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().rstrip().split()) # N: 사람의 수, K: 제거할 사람의 위치

nums = deque([i for i in range(1, N + 1)])
result = []

while nums:
  nums.rotate(-(K - 1))
  result.append(nums.popleft())

result = '<' + ', '.join(map(str, result)) + '>'

print(result)