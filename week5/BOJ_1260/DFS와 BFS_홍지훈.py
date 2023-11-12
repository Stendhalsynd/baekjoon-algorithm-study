import sys
from collections import deque

# N : 정점의 개수, M : 간선의 개수, V : 탐색을 시작할 정점의 번호
N, M, V = list(map(int,sys.stdin.readline().rstrip().split()))

# M 개 줄에 간선이 연결하는 두 정점의 번호
edges = [ tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(M)]

def create_adjacency_list(pairs):
  adjacency_list = {}

  for pair in pairs:
    node1, node2 = pair
    if node1 not in adjacency_list:
      adjacency_list[node1] = []
    if node2 not in adjacency_list:
      adjacency_list[node2] = []
    
    adjacency_list[node1].append(node2)
    adjacency_list[node2].append(node1)

  for key in adjacency_list:
    adjacency_list[key].sort()

  return adjacency_list

def dfs(graph, start, visited):
  if start not in graph.keys():
    return
  if start not in visited:
    visited.append(start)

    for neighbor in graph[start]:
      if neighbor not in visited:
        dfs(graph, neighbor, visited)

def bfs(graph, start, visited):
  if start not in graph.keys():
    return
  queue = deque([start])
  while queue:
    cur_v = queue.popleft()
    if cur_v not in visited:
      visited.append(cur_v)
    for node in graph[cur_v]:
      if node not in visited:
        visited.append(node)
        queue.append(node)

graph = create_adjacency_list(edges)
dfs_visited = []
bfs_visited = []

dfs(graph, V, dfs_visited)
bfs(graph, V, bfs_visited)

if not dfs_visited:
    dfs_visited = [V]

if not bfs_visited:
    bfs_visited = [V]

print(*dfs_visited)
print(*bfs_visited)