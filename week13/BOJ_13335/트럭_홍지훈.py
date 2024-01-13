import sys
input = sys.stdin.readline
from collections import deque

n, w, L = map(int, input().rstrip().split()) # n: 다리를 건너는 트럭의 수, w: 다리의 길이, L: 다리의 최대하중
weights = deque(list(map(int, input().rstrip().split()))) # weights: 트럭들의 무게

bridge = deque([0 for _ in range(w)])

curr_total = 0
time = 0

while weights:
  next_truck_count = w - bridge.count(0)
  if weights[0] + curr_total - bridge[0] <= L and next_truck_count <= w: # case 1. 다음 시간에 다리에 트럭이 올라갈 수 있는 경우 
    bridge.append(weights[0])
    curr_total += weights[0]
    curr_total -= bridge.popleft()
    weights.popleft()
    time += 1
  elif weights[0] + curr_total - bridge[0] <= L and next_truck_count > w or weights[0] + curr_total - bridge[0] > L: # case 2. 다음 시간에 다리에 트럭이 올라갈 하중은 되지만 길이가 꽉찬경우 / # case 3. 일단 다리가 더이상의 무게를 버티지 못할 경우
    curr_total -= bridge.popleft()
    bridge.append(0)
    time += 1

  if not weights and sum(bridge) > 0: # case 4. weights 를 모두 비웠을 때 마지막으로 추가한 트럭이 다리의 맨 앞에 위치하게 되었을 때
    time += w
print(time)

'''
case 1. weights, bridge, time, currtotal :  deque([4, 5, 6]) deque([0, 7]) 1 7
case 3. weights, bridge, time, currtotal :  deque([4, 5, 6]) deque([7, 0]) 2 7
case 1. weights, bridge, time, currtotal :  deque([5, 6]) deque([0, 4]) 3 4
case 1. weights, bridge, time, currtotal :  deque([6]) deque([4, 5]) 4 9
case 3. weights, bridge, time, currtotal :  deque([6]) deque([5, 0]) 5 5
case 4. weights, bridge, time, currtotal :  deque([]) deque([0, 6]) 6 6
        weights, bridge, time, currtotal :  deque([]) deque([6, 0]) 6 7
        weights, bridge, time, currtotal :  deque([]) deque([0, 0]) 0 8
'''