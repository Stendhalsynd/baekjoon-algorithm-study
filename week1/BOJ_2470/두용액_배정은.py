import sys

def mininum_water(N, water):
    minium, min_value = int(1e10), [0, 0]
    start, end = 0, (N - 1)

    while start < end:
        two_sum = water[start] + water[end]

        if minium > abs(two_sum):
            minium = abs(two_sum)
            min_value = [water[start], water[end]]
            if minium == 0:
                break

        if two_sum < 0: # 0 보다 작으므로 두 수의 합을 키워야 함
            start += 1
        else: # 0 보다 크므로 두 수의 합이 더 작아야 함
            end -= 1

    print(min_value[0], min_value[1])

N = int(sys.stdin.readline().rstrip()) # 전체 용액의 수
water = list(map(int, sys.stdin.readline().split()))
water.sort()# 오름차순으로 정렬
mininum_water(N, water)