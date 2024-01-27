import sys
import copy

R, C = map(int, sys.stdin.readline().split())
arr = []

for _ in range(R):
    arr.append(list(sys.stdin.readline().strip()))

printArr = copy.deepcopy(arr)

for i in range(R):
    for j in range(C):
        if arr[i][j] == 'X':
            count = 0
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = i + dx, j + dy
                if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] == 'X':
                    count += 1
            if count >= 3:
                printArr[i][j] = '.'

min_x, max_x, min_y, max_y = R, 0, C, 0

for i in range(R):
    for j in range(C):
        if printArr[i][j] == 'X':
            min_x = min(min_x, i)
            max_x = max(max_x, i)
            min_y = min(min_y, j)
            max_y = max(max_y, j)

for i in range(min_x, max_x+1):
    for j in range(min_y, max_y+1):
        print(printArr[i][j], end="")
    print()