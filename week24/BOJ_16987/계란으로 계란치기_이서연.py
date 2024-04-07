import sys

input = sys.stdin.readline

N = int(input().strip())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

def backtracking(n, cnt):
    global result

    if n == N:
        result = max(result, cnt)
        return

    if graph[n][0] <= 0:
        backtracking(n + 1, cnt)
    else:
        flag = False

        for i in range(N):
            if n == i or graph[i][0] <= 0:
                continue

            flag = True

            graph[n][0] -= graph[i][1]
            graph[i][0] -= graph[n][1]

            backtracking(n + 1, cnt + int(graph[n][0] <= 0) + int(graph[i][0] <= 0))

            graph[n][0] += graph[i][1]
            graph[i][0] += graph[n][1]

        if flag == False:
            backtracking(n + 1, cnt)


result = 0

backtracking(0 , 0)

print(result)