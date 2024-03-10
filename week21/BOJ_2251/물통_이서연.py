import sys
from collections import deque

input = sys.stdin.readline

A, B, C = map(int, input().split())

def pour(x, y, queue):
    if not visited[x][y]:
        visited[x][y] = True
        queue.append((x, y))

def bfs(answer):
    visited[0][0] = True
    queue = deque()
    queue.append((0, 0))

    while queue:
        a, b = queue.popleft()
        c = C - a - b

        if a == 0:
            answer.append(c)

        water = min(a, B - b)
        pour(a - water, b + water, queue)

        water = a
        pour(a - water, b, queue)

        water = min(b, A - a)
        pour(a + water, b - water, queue)

        water = b
        pour(a, b - water, queue)

        water = min(c, A - a)
        pour(a + water, b, queue)

        water = min(c, B - b)
        pour(a, b + water, queue)

visited = [[False] * (B + 1) for _ in range(A + 1)]

answer = []

bfs(answer)

answer.sort()

for i in answer:
    print(i, end=" ")