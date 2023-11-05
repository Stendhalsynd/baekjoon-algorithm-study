# 특정 위치를 기준으로 양 옆에 자신보다 작은 높이의 블록이 있다면 해당 위치에는 물이 고일 수 있다.
# 이 조건에 만족할 때 물이 고이는 양은 왼쪽과 오른쪽 블록 중 더 낮은 블록과 현 위치의 값이다.
# 만약 높이가 1인 구역을 왼쪽 으론쪽으로 3, 4 높이의 블록이 있다고 하면 해당 구역은 더 낮은 블록인 3에서 현 위치의 높이인 1을 뺀 1만큼의 물이 고인다
# 첫 번째 칸과 마지막칸은 물이 고일 수 없으므로 1 ~ (w-1)까지 잡아주고 각 위치마다 알맞은 양의 물을 채워넣으면 된다.

import sys

h, w = map(int, input().split()) # 세로 길이 h, 가로 길이 w
block = list(map(int, input().split())) # 쌓인 높이

ans = 0

for i in range(1, w-1):
    left_max = max(block[:i])
    right_max = max(block[i+1:])

    temp = min(left_max, right_max)

    if block[i] <= temp:
        ans += temp - block[i]

print(ans)