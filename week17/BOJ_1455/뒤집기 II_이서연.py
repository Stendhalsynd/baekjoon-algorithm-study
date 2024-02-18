import sys

input = sys.stdin.readline

N, M = map(int, input().split())

square = []

for _ in range(N):
    square.append(list(map(int, input().strip())))

def flip(x, y):
    for i in range(x + 1):
        for j in range(y + 1):
            if square[i][j] == 0:
                square[i][j] = 1
            else:
                square[i][j] = 0

cnt = 0

for i in range(N - 1, -1, -1):
    for j in range(M - 1, -1, -1):
        if square[i][j] == 1:
            cnt += 1
            flip(i, j)

print(cnt)