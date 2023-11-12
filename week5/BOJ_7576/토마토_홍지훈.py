import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    global fresh_tomatoes
    if not contain_not_ripen():
        return 0

    count = 0
    while queue:
        lenQ = len(queue)
        for _ in range(lenQ):
            y, x = queue.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0 <= nx < M and tomato[ny][nx] == 0:
                    tomato[ny][nx] = 1
                    queue.append((ny, nx))
                    fresh_tomatoes -= 1  # 새로 익은 토마토 갯수 갱신
        count += 1
        if fresh_tomatoes == 0:
            return count

def contain_not_ripen():
    return fresh_tomatoes > 0

# M : 상자의 가로 칸 수
# N : 상자의 세로 칸 수
M, N = map(int, input().rstrip().split())
tomato = [list(map(int, input().rstrip().split())) for _ in range(N)]

# 상, 하, 좌, 우
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

queue = deque((r, c) for r in range(N) for c in range(M) if tomato[r][c] == 1)
fresh_tomatoes = sum(row.count(0) for row in tomato)  # 익지 않은 토마토 갯수 초기화

count = bfs()

if fresh_tomatoes > 0:
    count = -1

print(count)
