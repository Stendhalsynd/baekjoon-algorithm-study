import heapq
import sys 
input = sys.stdin.readline
INF = int(1e9)

N = int(input()) # N : 정점의 개수

graph = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
  info = map(int, input().split())
  graph[i].extend([j + 1 for j, val in enumerate(info) if val == 1])

def dijkstra(start, answer):
  que = []
  heapq.heappush(que, (0, start)) # 우선순위 큐 que 에 시작노드 start 까지의 최단 거리는 0이다.
  while que:
    dist, now = heapq.heappop(que) # que 에 넣은 튜플 (dist, now) dist 는 거리, now 는 노드
    if answer[now] < dist: # 갱신하지 않는 경우
      continue
    for next in graph[now]: # 현재 노드 now 에서 갈 수 있는 노드 next
      new_dist = dist + 1
      if new_dist < answer[next]:
        answer[next] = new_dist
        heapq.heappush(que, (new_dist, next))
  return answer

matrix = [[0] * N for _ in range(N)]

for i in range(1, N + 1):
  answer = {node: INF for node in range(1, N + 1)}
  now = dijkstra(i, answer)

  for j, val in enumerate(now.values()):
    if val != INF:
      matrix[i - 1][j] = 1

for row in matrix:
  for col in row:
    print(col, end=' ')
  print()

# 플로이드 - 워셜 알고리즘
# import sys 
# input = sys.stdin.readline
# INF = int(1e9)

# N = int(input()) # N : 정점의 개수

# graph = [[INF] * (N + 1) for _ in range(N + 1)]

# for i in range(1, N + 1):
#   info = map(int, input().split())
#   for j, val in enumerate(info):
#     if val == 1:
#       graph[i][j + 1] = 1

# for k in range(1, N + 1):
#   for a in range(1, N + 1):
#     for b in range(1, N + 1):
#       graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# for a in range(1, N + 1):
#   for b in range(1, N + 1):
#     if graph[a][b] != INF:
#       print(1, end=' ')
#     else:
#       print(0, end=' ')
#   print()