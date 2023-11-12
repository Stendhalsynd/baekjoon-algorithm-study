# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
import sys
from collections import deque

N = int(sys.stdin.readline().rstrip()) # 컴퓨터의 수
M = int(sys.stdin.readline().rstrip()) # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수

matrix = [[0] * N for _ in range(N)]
visited = [False] * N

for _ in range(M):
  i, j = map(int, input().split())
  matrix[i-1][j-1] = 1
  matrix[j-1][i-1] = 1

queue = deque([1])
visited[0] = True

def bfs():
  count = 0
  while queue:
    node = queue.popleft()

    for idx, val in enumerate(matrix[node - 1]):
      if val == 1 and visited[idx] is False:
        queue.append(idx + 1)
        visited[idx] = True
        count += 1
  return count

print(bfs())

# # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수
# pairs = [ tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M)]

# visited = set()

# def create_adjacency_list(pairs):
#   adjacency_list = {}

#   for pair in pairs:
#     node1, node2 = pair
#     if node1 not in adjacency_list:
#       adjacency_list[node1] = []
#     if node2 not in adjacency_list:
#       adjacency_list[node2] = []
    
#     adjacency_list[node1].append(node2)
#     adjacency_list[node2].append(node1)

#   return adjacency_list

# def dfs(graph, start, visited):
#   if start not in graph.keys():
#     return
#   if start not in visited:
#     visited.add(start)

#     for neighbor in graph[start]:
#       if neighbor not in visited:
#         dfs(graph, neighbor, visited)

# graph = create_adjacency_list(pairs)

# dfs(graph, 1, visited)
# if 1 in visited:
#   visited.remove(1)

# print(len(visited))
