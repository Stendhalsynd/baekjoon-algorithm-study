from heapq import heappush, heappop
import sys
input = sys.stdin.readline

INF = int(1e9)
result = 1
result_sum = INF
N, M = map(int, input().split()) # N: 유저의 수, M: 친구 관계의 수
graph = [[] for i in range(N + 1)] # 연결 리스트 graph

for _ in range(M):
  A, B = map(int, input().split())
  graph[A].append(B) # A 에서 B 로 가는 경로가 존재
  graph[B].append(A) # B 에서 A 로 가는 경로가 존재

def dijkstra(start):
  que = [] 
  answer = {node: INF for node in range(1, N + 1)} # 최단 거리를 기록할 answer
  heappush(que, (0, start)) # 우선순위 큐 que 에 시작노드 start 까지의 최단 거리는 0이다.
  answer[start] = 0
  while que:
    dist, now = heappop(que) # que 에 넣은 튜플 (dist, now) dist 는 거리, now 는 노드
    if answer[now] < dist: # 갱신하지 않는 경우
      continue
    for next in graph[now]: # 현재 노드 now 에서 갈 수 있는 노드 next
      n_dist = dist + 1
      if n_dist < answer[next]:
        answer[next] = n_dist
        heappush(que, (n_dist, next))
  return answer


for i in range(1, N + 1):
  curr = sum(dijkstra(i).values())
  if curr < result_sum:
    result = i
    result_sum = curr
    
print(result)