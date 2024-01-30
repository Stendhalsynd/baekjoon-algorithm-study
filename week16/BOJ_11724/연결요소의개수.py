import sys

sys.setrecursionlimit(2000) 
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]  # [[], [2, 5], [1, 5, 4, 3], [4, 2], [3, 6, 5, 2], [2, 1, 4], [4]]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def DFS(x):
    if not visited[x]:
        visited[x] = True
    
    for node in graph[x]:
        if not visited[node]:
            DFS(node)

count = 0
for i in range(1, n + 1):
    if not visited[i]:
        DFS(i)
        count += 1
print(count)