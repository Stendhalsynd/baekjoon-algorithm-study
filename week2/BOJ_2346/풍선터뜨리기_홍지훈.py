import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

deq = deque([(val, idx + 1) for idx, val in enumerate(nums)])  
result = []

for num in nums:
  doc = deq.popleft()
  val, idx = doc

  result.append(idx)
  if deq:
    if val > 0:
      for i in range(val - 1):
        deq.append(deq.popleft())
    else:
      for i in range(-val):
        deq.appendleft(deq.pop())

for val in result:
  print(val)