import sys


def bingo(maps):
    count = 0
    if sum([maps[i][i] for i in range(5)]) == 0: count += 1
    if sum([maps[i][4 - i] for i in range(5)]) == 0: count += 1

    for i in range(5):
        if sum(maps[i]) == 0: count += 1
        if sum([maps[j][i] for j in range(5)]) == 0: count += 1

    return count


maps_coord = dict()
maps = [[0 for _ in range(5)] for _ in range(5)]
for idx in range(5):
    maps[idx] = list(map(int, sys.stdin.readline().split()))
    for map_idx in range(len(maps)):
        maps_coord[maps[idx][map_idx]] = [idx, map_idx]

flag = False
bingo_num = 0
for idx in range(5):
    numbers = list(map(int, sys.stdin.readline().split()))
    for num_idx in range(len(numbers)):
        coord = maps_coord[numbers[num_idx]]
        maps[coord[0]][coord[1]] = 0

        if flag is False and bingo(maps) >= 3:
            bingo_num = idx * 5 + (num_idx + 1)
            flag = True
print(bingo_num)