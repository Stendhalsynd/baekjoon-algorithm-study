import sys
import copy

input = sys.stdin.readline

R, C = map(int, input().split())

maps = []

for i in range(R):
    maps.append(list(str(input().strip())))

new_maps = copy.deepcopy(maps)

for i in range(R):
    for j in range(C):
        cnt = 0

        if maps[i][j] == 'X':
            if i - 1 < 0 or maps[i - 1][j] == ".":
                cnt += 1
            
            if j - 1 < 0 or maps[i][j - 1] == ".":
                cnt += 1
            
            if i + 1 >= R or maps[i + 1][j] == ".":
                cnt += 1
            
            if j + 1 >= C or maps[i][j + 1] == ".":
                cnt += 1
            
            if cnt >= 3:
                new_maps[i][j] = "."

top, left, bottom, right = R - 1, C - 1, 0, 0

for i in range(R):
    for j in range(C):
        if new_maps[i][j] == "X":
            top = min(top, i)
            left = min(left, j)
            bottom = max(bottom, i)
            right = max(right, j)

for i in range(top, bottom + 1):
    for j in range(left, right + 1):
        print(new_maps[i][j], end = "")
    
    print()