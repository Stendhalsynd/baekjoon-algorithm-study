N, M, V = map(int, input().split())
adj_list = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

for i in range(N+1):
    adj_list[i].sort()

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]: # v와 연결된 노드들 중
        if not visited[i]: # 방문하지 않은 노드가 있다면
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = [v]
    visited[v] = True
    while queue:
        current_v = queue.pop(0)
        print(current_v, end=' ')
        for i in graph[current_v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs(adj_list, V, visited)
print()
visited = [False] * (N+1)
bfs(adj_list, V, visited)