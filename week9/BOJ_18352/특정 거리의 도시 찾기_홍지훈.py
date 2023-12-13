import heapq
import sys 
input = sys.stdin.readline
INF = int(1e9)

N, M, K, X = map(int, input().split()) # N : 도시의 개수, M : 도로의 개수, K : 거리 정보, X : 출발 도시의 번호

# 최단 거리를 기록할 answer
answer = {node: INF for node in range(1, N + 1)}

# 연결 리스트 graph
graph = [[] for i in range(N + 1)]
for _ in range(M):
  A, B = map(int, input().split())
  graph[A].append(B) # A 에서 B 로 가는 경로가 존재

def dijkstra(start):
  que = []
  heapq.heappush(que, (0, start)) # 우선순위 큐 que 에 시작노드 start 까지의 최단 거리는 0이다.
  answer[start] = 0
  while que:
    dist, now = heapq.heappop(que) # que 에 넣은 튜플 (dist, now) dist 는 거리, now 는 노드
    if answer[now] < dist: # 갱신하지 않는 경우
      continue
    for next in graph[now]: # 현재 노드 now 에서 갈 수 있는 노드 next
      new_dist = dist + 1
      if new_dist < answer[next]:
        answer[next] = new_dist
        heapq.heappush(que, (new_dist, next))

dijkstra(X)

if K not in answer.values():
  print(-1)
else:
  for i in range(1, N + 1):
    if answer[i] == K:
      print(i)