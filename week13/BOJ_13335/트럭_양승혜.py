"""
4 2 10
7 4 5 6
"""
# 큐 사용

from collections import deque

count = 0

n, w, l = map(int, input().split())
trains = deque(map(int, input().split()))

bridge = deque([0] * w)

while bridge:
    count += 1
    bridge.popleft()
    if trains:
        if sum(bridge) + trains[0] <= l:
            bridge.append(trains.popleft())
        else:
            bridge.append(0)

print(count)
    
# 리스트 사용

count = 0

n, w, l = map(int, input().split())
trains = list(map(int, input().split()))

bridge = [0] * w

while bridge:
    count += 1
    bridge.pop(0)
    if trains:
        if sum(bridge) + trains[0] <= l:
            bridge.append(trains.pop(0))
        else:
            bridge.append(0)

print(count)
