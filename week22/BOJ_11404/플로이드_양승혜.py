import sys
input = sys.stdin.readline

n = int(input())
bus = int(input())
graph = [[1e9] * (n + 1) for _ in range(n + 1)]
for _ in range(bus):
    a, b, c = map(int, input().split())
    graph[a][b] = min(c, graph[a][b])

for i in range(n + 1):
    for j in range(n + 1):
        if i == j:
            graph[i][j] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for r in range(1, n + 1):
    for c in range(1, n + 1):
        if graph[r][c] == 1e9:
            print(0, end = " ")
        else:
            print(graph[r][c], end = " ")
    print()
