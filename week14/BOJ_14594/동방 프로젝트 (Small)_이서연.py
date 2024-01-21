import sys

input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())

rooms = [1] * (N - 1)

movings = []

for i in range(M):
    movings.append(tuple(map(int, input().split())))

for i, j in movings:
    for k in range(j -i):
        rooms[i - 1 + k] = 0

print(sum(rooms) + 1)