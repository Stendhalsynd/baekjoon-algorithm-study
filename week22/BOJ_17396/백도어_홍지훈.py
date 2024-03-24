from heapq import heappush, heappop
import sys
input = sys.stdin.readline
INF = int(1e11)

N, M = map(int, input().split()) # N: 분기점의 수, M: 간선의 개수
sights = list(map(int, input().split())) # a1, a2, ... an-1
graph = [[] for i in range(N + 1)] # 연결 리스트 graph

for _ in range(M):
  a, b, t = map(int, input().split()) # a 번째 분기점과 b 번째 분기점을 지나는데 t만큼 시간소요
  graph[a].append((b, t))
  graph[b].append((a, t))

def dijkstra():
  que = []
  answer = {node: INF for node in range(N)} # 최단 거리를 기록할 answer
  heappush(que, (0, 0))
  answer[0] = 0
  while que:
    dist, now = heappop(que)
    if answer[now] < dist:
      continue
    for next in graph[now]:
      if next[0] < N - 1 and sights[next[0]]: continue
      new_dist = dist + next[1]
      if new_dist < answer[next[0]]:
        answer[next[0]] = new_dist
        heappush(que, (new_dist, next[0]))
  return answer[N - 1]

result = dijkstra()
print(-1 if result >= INF else result)