n, d = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(n)]
graph = [_ for _ in range(d + 1)]


for i in range(d + 1):
    graph[i] = min(graph[i], graph[i - 1] + 1)
    for start, end, cost in info:
        if end <= d and i == start:
            graph[end] = min(graph[start] + cost, graph[end])
print(graph[-1])
