import sys

input = sys.stdin.readline

N = int(input().strip())
graph = list(map(str, input().strip()))

count = 0

for i in range(1, N):
    if graph[i] == 'W' and graph[i - 1] == 'E':
        count += 1

print(count)