n = int(input())
m = int(input())

matrix = [[0] * n for _ in range(n)]
visited = [False] * n

for _ in range(m):
    i, j = map(int, input().split())
    matrix[i-1][j-1] = 1
    matrix[j-1][i-1] = 1

def dfs(matrix, i, visited):
    visited[i] = True
    for k in range(len(matrix[i])):
        if matrix[i][k] == 1 and not visited[k]:
            dfs(matrix, k, visited)

dfs(matrix, 0, visited)
print(visited.count(True) - 1)