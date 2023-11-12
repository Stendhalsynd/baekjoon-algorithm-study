import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
pairs = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().rstrip().split())
    pairs[B].append(A)

def bfs(start_v):
    count = 1
    visited = [False for _ in range(N + 1)]
    visited[start_v] = True
    queue = deque([start_v])
    while queue:
        cur_v = queue.popleft()  
        for v in pairs[cur_v]:
            if not visited[v]:
                visited[v] = True
                count += 1
                queue.append(v)
    return count

maxValue = 0
output = []

for key in range(1, N + 1):
    count = bfs(key)
    if count > maxValue:
        maxValue = count
        output.clear()
        output.append(key)
    elif count == maxValue:
        output.append(key)

print(*output)
