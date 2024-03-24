import sys

input = sys.stdin.readline

n = int(input().strip())

alphabet = "abcdefghijklmnopqrstuvwxyz"

INF = sys.maxsize
graph = [[INF] * len(alphabet) for _ in range(len(alphabet))]

for _ in range(n):
    x, y, z = map(str, input().split())
    graph[alphabet.index(x)][alphabet.index(z)] = 1

for k in range(len(alphabet)):
    for a in range(len(alphabet)):
        for b in range(len(alphabet)):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

m = int(input().strip())

for _ in range(m):
    x, y, z = map(str, input().split())
    if graph[alphabet.index(x)][alphabet.index(z)] == INF:
        print("F")
    else:
        print("T")
