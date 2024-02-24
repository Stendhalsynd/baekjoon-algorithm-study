import sys
import copy

input = sys.stdin.readline

n, m, h = map(int, input().split())

blocks = []

for i in range(n):
    blocks.append(list(map(int, input().split())))

d = [[1] + [0] * h for i in range(n + 1)]

for i in range(1, n + 1):
    d[i] = copy.deepcopy(d[i - 1])
    
    for b in blocks[i - 1]:
        for j in range(b, h + 1):
            d[i][j] += d[i - 1][j - b]

print(d[-1][-1] % 10007)