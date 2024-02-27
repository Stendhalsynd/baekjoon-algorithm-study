h, w = map(int, input().split())
stickers = []

for _ in range(int(input())):
    a, b = map(int, input().split())
    if a <= max(h, w) and b <= max(h, w):
        stickers.append([a, b])

answer = 0
for i in range(len(stickers)):
    for j in range(i + 1, len(stickers)):
        r1, c1 = stickers[i]
        r2, c2 = stickers[j]
        if (r1 + r2 <= h and max(c1, c2) <= w) or (max(r1, r2) <= h and c1 + c2 <= w):
            answer = max(answer, (r1 * c1) + (r2 * c2))
        if (r1 + c2 <= h and max(c1, r2) <= w) or (max(r1, c2) <= h and c1 + r2 <= w):
            answer = max(answer, (r1 * c1) + (r2 * c2))
        if (c1 + r2 <= h and max(r1, c2) <= w) or (max(c1, r2) <= h and r1 + c2 <= w):
            answer = max(answer, (r1 * c1) + (r2 * c2))
        if (c1 + c2 <= h and max(r1, r2) <= w) or (max(c1, c2) <= h and r1 + r2 <= w):
            answer = max(answer, (r1 * c1) + (r2 * c2))

print(answer)
