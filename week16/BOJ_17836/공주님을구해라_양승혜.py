from collections import deque

n, m, curse = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

def BFS():
    sword = 1e9
    queue = deque([(0, 0)])
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        a, b = queue.popleft()
        if a == n - 1 and b == m - 1:
            return min(visited[a][b], sword)
        if graph[a][b] == 2:
            sword = visited[a][b] + n - 1 - a + m - 1 - b
        for move in moves:
            A, B = a + move[0], b + move[1]
            if 0 <= A < n and 0 <= B < m and not visited[A][B] and graph[A][B] != 1:
                visited[A][B] = visited[a][b] + 1
                queue.append((A, B))
    return sword

answer = BFS()
print("Fail" if answer > curse else answer)