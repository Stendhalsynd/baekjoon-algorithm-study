import sys

def water_position_check(position, water_position, L, count):
    next_position = position
    for idx in range(position + 1, len(water_position)):
        if water_position[idx] - water_position[position] < L:
            next_position = idx
        else:
            return next_position, count + 1

    return next_position, count + 1

N, L = map(int, sys.stdin.readline().split()) # 물이 새는 곳 N, 테이프 길이 L
water_position = sorted(list(map(int, sys.stdin.readline().split()))) # 물이 새는 곳의 위치

idx, count = 0, 0
while idx < N:
    idx, count = water_position_check(idx, water_position, L, count)
    idx += 1

print(count)
