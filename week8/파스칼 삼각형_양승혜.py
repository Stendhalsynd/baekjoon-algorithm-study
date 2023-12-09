import math

nums = 0
r, c, w = map(int, input().split())
for i in range(w):
    for j in range(i + 1):
        nums += math.comb(r - 1 + i, c - 1 + j)
print(nums)
