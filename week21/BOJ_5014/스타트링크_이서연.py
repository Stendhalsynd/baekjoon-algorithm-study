import sys
from collections import deque

input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())

def bfs(visited, S):
    count = 0
    visited[S] = 1

    queue = deque()
    queue.append(S)

    while queue:
        x = queue.popleft()

        if x == G:
            return count

        if x < G:
            if U != 0 and x + U <= F and visited[x + U] == 0:
                visited[x + U] = 1
                queue.append(x + U)
                count += 1
            elif D != 0 and x - D >= 1 and visited[x - D] == 0:
                visited[x - D] = 1
                queue.append(x - D)
                count += 1
        elif x > G:
            if D != 0 and x - D >= 1 and visited[x - D] == 0:
                visited[x - D] = 1
                queue.append(x - D)
                count += 1
            elif U != 0 and x + U <= F and visited[x + U] == 0:
                visited[x + U] = 1
                queue.append(x + U)
                count += 1

    return -1

visited = [0] * (F + 1)
result = bfs(visited, S)

if result == -1:
    print("use the stairs")
else:
    print(result)