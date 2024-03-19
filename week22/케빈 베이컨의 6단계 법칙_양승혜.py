# 플로이드 - 워셜
n, m = map(int, input().split())
graph = [[1e9] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    f1, f2 = map(int, input().split())
    graph[f1][f2] = 1
    graph[f2][f1] = 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

dist = 1e9
answer = 0
for i in range(n + 1):
    total = sum(graph[i][1:])
    if dist > total:
        dist = total
        answer = i

print(answer)


# bfs
from collections import deque

def bfs(graph, start):
    visited = [False] * (n + 1)
    dist = [0] * (n + 1)
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dist[neighbor] = dist[node] + 1
                visited[neighbor] = True
                queue.append(neighbor)
    return sum(dist)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

minDist = 1e9
answer = 0
for i in range(1, n + 1):
    total = bfs(graph, i)
    if minDist > total:
        minDist = total
        answer = i

print(answer)
