import sys
input = sys.stdin.readline

H, W = map(int, input().rstrip().split())  # 모눈종이의 크기 H, W
N = int(input().rstrip())  # N: 스티커의 수
stickers = []

for _ in range(N):
    R, C = map(int, input().rstrip().split())
    stickers.append((R, C))

max_area = 0

for i in range(N):
    for j in range(i + 1, N):
        r1, c1 = stickers[i]
        r2, c2 = stickers[j]

        if r1 + r2 <= H and max(c1, c2) <= W:  
            max_area = max(max_area, r1 * c1 + r2 * c2)
        if c1 + c2 <= H and max(r1, r2) <= W:  
            max_area = max(max_area, r1 * c1 + r2 * c2)
        if r1 + r2 <= W and max(c1, c2) <= H:  
            max_area = max(max_area, r1 * c1 + r2 * c2)
        if c1 + c2 <= W and max(r1, r2) <= H:  
            max_area = max(max_area, r1 * c1 + r2 * c2)

        if r1 + c2 <= H and max(c1, r2) <= W:  
            max_area = max(max_area, r1 * c1 + r2 * c2)
        if c1 + r2 <= H and max(r1, c2) <= W:  
            max_area = max(max_area, r1 * c1 + r2 * c2)
        if r1 + c2 <= W and max(c1, r2) <= H:  
            max_area = max(max_area, r1 * c1 + r2 * c2)
        if c1 + r2 <= W and max(r1, c2) <= H:  
            max_area = max(max_area, r1 * c1 + r2 * c2)
            
print(max_area)