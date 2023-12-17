n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

for k in range(n):  # 지나가는 정점
    for i in range(n):  # 출발하는 정점
        for j in range(n):  # 도착 정점
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for row in graph:
    print(" ".join(map(str, row)))
