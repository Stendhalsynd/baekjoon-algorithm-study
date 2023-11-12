N = int(input())
adj_list = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(N-1):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

def bfs(graph, v, visited):
    parent_lst = [0] * (N+1)
    queue = [v]
    visited[v] = True
    while queue:
        current_v = queue.pop(0)
        for i in graph[current_v]:
            if not visited[i]:
                parent_lst[i] = current_v
                queue.append(i)
                visited[i] = True
    return parent_lst

parent_lst = bfs(adj_list, 1, visited)
print('\n'.join(map(str, parent_lst[2:])))