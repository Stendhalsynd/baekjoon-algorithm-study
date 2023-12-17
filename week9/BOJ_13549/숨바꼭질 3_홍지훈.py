from heapq import heappop, heappush
import sys 
input = sys.stdin.readline
INF = int(1e9)
MAX = 100000

N, K = map(int, input().split()) # N : 수빈이가 있는 위치, K : 동생이 있는 위치

# 걷기 : 1초뒤 +1 or -1
# 순간이동 : 0초뒤 2 * X 

# 최단거리 기록
answer = {node: INF for node in range(MAX + 1)}

# 연결 관계 graph
graph = [[] for i in range(MAX + 1)]
for i in range(MAX + 1):
  if i == 0:
    graph[i].append((1, 1))
  elif i == MAX:
    graph[i].append((MAX - 1, 1))
  else:
    graph[i].append((i + 1, 1))
    graph[i].append((i - 1, 1))
    if i * 2 <= MAX:
      graph[i].append((i * 2, 0))

def dijkstra(start):
  que = []
  heappush(que, (0, start))
  answer[start] = 0
  while que:
    dist, now = heappop(que)
    if answer[now] < dist:
      continue
    for info in graph[now]:
      next, new_dist = info
      distance = dist + new_dist
      if distance < answer[next]:
        answer[next] = distance
        heappush(que, (distance, next))

dijkstra(N)

print(answer[K])