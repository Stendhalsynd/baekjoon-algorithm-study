from heapq import heappush, heappop
import sys
input = sys.stdin.readline
INF = int(1e9)

N, E = map(int, input().split()) # N: 정점의 개수, E: 간선의 개수
graph = [[] for i in range(N + 1)] # 연결 리스트 graph

for _ in range(E):
  a, b, c = map(int, input().split()) # a 번 정점에서 b 번 정점까지 양방향 길 존재, 거리가 c
  graph[a].append((b, c))
  graph[b].append((a, c))

v1, v2 = map(int, input().split()) # v1, v2 는 반드시 거쳐야 하는 두 개의 서로 다른 정점

def dijkstra(start):
  que = []
  answer = {node: INF for node in range(1, N + 1)} # 최단 거리를 기록할 answer
  heappush(que, (0, start))
  answer[start] = 0
  while que:
    dist, now = heappop(que)
    if answer[now] < dist:
      continue
    for next in graph[now]:
      new_dist = dist + next[1]
      if new_dist < answer[next[0]]:
        answer[next[0]] = new_dist
        heappush(que, (new_dist, next[0]))
  return answer

'''
1 -> v1 -> v2 -> N
1 -> v2 -> v1 -> N
caution! case1, case2 중 하나의 값이 INF 보다 커질수도 있습니다
'''

case1 = dijkstra(1)[v1] + dijkstra(v1)[v2] + dijkstra(v2)[N]
case2 = dijkstra(1)[v2] + dijkstra(v2)[v1] + dijkstra(v1)[N]

result = min(case1, case2)
print(-1 if result >= INF else result)