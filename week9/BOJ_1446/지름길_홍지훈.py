from heapq import heappush, heappop
import sys
input = sys.stdin.readline
INF = 10000

N, D = map(int,input().split()) # N : 지름길의 개수, D : 고속도로의 길이

answer = {node: INF for node in range(D + 1)}

graph = [[] for i in range(D + 1)]

for i in range(D): 
  for j in range(i + 1, D + 1):
    graph[i].append((j, j - i))

for _ in range(N):
  start, end, dist = map(int, input().split())
  if start < end and start < D: # 시작점이 목적지보다 큰 지름길이 주어질 수 있다.
    graph[start].append((end, dist)) # start 에서 end 로 가는 지름길의 길이가 dist 이다.

def dijkstra():
  que = []
  heappush(que, (0, 0))
  answer[0] = 0
  while que:
    dist, now = heappop(que)
    if answer[now] < dist or now > D:
      continue
    for next in graph[now]:
      new_dist = dist + next[1]
      if next[0] <= D and new_dist < answer[next[0]]:
        answer[next[0]] = new_dist
        heappush(que, (new_dist, next[0]))

dijkstra()

print(answer[D])