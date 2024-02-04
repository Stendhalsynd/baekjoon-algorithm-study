import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().rstrip().split()) # N: 정점의 개수, M: 간선의 개수
pairs = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
for _ in range(M):
  u, v = map(int, input().rstrip().split())
  pairs[v].append(u)
  pairs[u].append(v)

def bfs(node: int) -> int:
  visited[node] = True
  q = deque([node])
  while q:
    cur = q.popleft()
    for next in pairs[cur]:
      if not visited[next]:
        visited[next] = True
        q.append(next)

result = 0
for key in range(1, N + 1):
  if not visited[key]:
    bfs(key)
    result += 1

print(result)