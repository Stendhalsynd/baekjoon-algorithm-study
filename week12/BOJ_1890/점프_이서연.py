import sys

input = sys.stdin.readline

size = int(input())

game = []

for i in range(size):
    game.append(list(map(int, input().split())))

d = [[0 for col in range(size)] for row in range(size)]
d[0][0] = 1

for i in range(size):
    for j in range(size):
        if i == size - 1 and j == size - 1:
            print(d[i][j])
            break
            
        if d[i][j] != 0 and j + game[i][j] < size:
            d[i][j + game[i][j]] += d[i][j]
            
        if d[i][j] != 0 and i + game[i][j] < size:
            d[i + game[i][j]][j] += d[i][j]
