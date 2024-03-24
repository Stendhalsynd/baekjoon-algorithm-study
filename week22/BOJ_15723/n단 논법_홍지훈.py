from heapq import heappush, heappop
import sys
input = sys.stdin.readline

INF = int(1e9)
graph = [[] for i in range(27)] # 연결 리스트 graph
result = []

def split(string: str):
  split_str = string.split('is')
  before = split_str[0].strip()
  after = split_str[1].strip()
  return before, after

def alphabet_to_number(letter):
  return ord(letter.lower()) - ord('a') + 1
  
def dijkstra(start, end):
  que = []
  answer = {node: INF for node in range(1, 27)} # 최단 거리를 기록할 answer
  heappush(que, (0, start)) # 우선순위 큐 que 에 시작노드 start 까지의 최단 거리는 0이다.
  answer[start] = 0
  while que:
    dist, now = heappop(que) # que 에 넣은 튜플 (dist, now) dist 는 거리, now 는 노드
    if answer[now] < dist: # 갱신하지 않는 경우
      continue
    for next in graph[now]: # 현재 노드 now 에서 갈 수 있는 노드 next
      new_dist = dist + 1
      if new_dist < answer[next]:
        answer[next] = new_dist
        heappush(que, (new_dist, next))
  return 'T' if answer[end] != INF else 'F'

n = int(input().rstrip()) # n: 정수
for _ in range(n):
  thesis = input()
  a, b = split(thesis)
  graph[alphabet_to_number(a)].append(alphabet_to_number(b))

m = int(input().rstrip())
for _ in range(m):
  thesis = input()
  a, b = split(thesis)
  start, end = alphabet_to_number(a), alphabet_to_number(b)
  result.append(dijkstra(start, end))

[print(v) for v in result]