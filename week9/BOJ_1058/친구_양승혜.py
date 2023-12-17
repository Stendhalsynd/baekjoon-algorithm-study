n = int(input())
friends = [list(input()) for _ in range(n)]
graph = [[0] * n for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if ((friends[i][k] == "Y" and friends[k][j] == "Y") and i != j) or friends[i][j] == "Y":
                graph[i][j] = 1

answer = -1
for row in graph:
    answer = max(answer, sum(row))
print(answer)
