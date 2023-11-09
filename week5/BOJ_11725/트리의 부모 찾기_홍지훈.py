# 그래프 이론, 그래프 탐색, 트리, 너비 우선 탐색, 깊이 우선 탐색
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input().rstrip())
edges = [ tuple(map(int, input().rstrip().split())) for _ in range(N-1)]

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

  return adjacency_list

adjacency_list = create_adjacency_list(edges)

parent_info = {i: 0 for i in range(2, N + 1)}
visited = set()

def find_parent(parent, adjacency_nodes):
  parents = []
  visited.add(parent)
  for node in adjacency_nodes:
    if node in visited:
      continue
    parent_info[node] = parent
    parents.append(node)

  for p in parents:
    if p not in visited:
      find_parent(p, adjacency_list[p])

find_parent(1, adjacency_list[1])

[print(parent_info[key]) for key in sorted(parent_info.keys())]
