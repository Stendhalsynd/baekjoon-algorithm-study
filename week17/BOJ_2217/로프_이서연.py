import sys

input = sys.stdin.readline

N = int(input().strip())

ropes = []

for _ in range(N):
    ropes.append(int(input().strip()))

ropes.sort(reverse=True)

result = 0
cnt = 0

for i in ropes:
    cnt += 1
    result = max(result, i * cnt)

print(result)