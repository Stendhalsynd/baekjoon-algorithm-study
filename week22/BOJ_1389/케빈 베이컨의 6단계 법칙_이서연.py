import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(x, visited):
    visited[x] = 0

    queue = deque()
    queue.append(x)

    while queue:
        p = queue.popleft()

        for i in graph[p]:
            if visited[i] == -1:
                visited[i] = visited[p] + 1
                queue.append(i)

    return sum(visited) + 1

numbers = []

for i in range(1, N + 1):
    visited = [-1] * (N + 1)
    numbers.append(bfs(i, visited))

minimum = min(numbers)
print(numbers.index(minimum) + 1)
