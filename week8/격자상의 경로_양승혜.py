row, column, k = map(int, input().split())

graph = [[0] * column for _ in range(row)]

def path(n, m):
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                graph[i][j] = 1
            else:
                graph[i][j] = graph[i - 1][j] + graph[i][j - 1]
    return graph[n - 1][m - 1]

if k == 0:
    print(path(row, column))

else:
    x = (k - 1) // column + 1
    y = k - (x - 1) * column
    part1 = path(x, y)
    part2 = path(row - x + 1, column - y + 1)
    print(part1 * part2)
