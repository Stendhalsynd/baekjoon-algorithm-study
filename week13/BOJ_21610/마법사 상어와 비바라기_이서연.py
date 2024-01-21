import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
ds = [list(map(int, input().split())) for _ in range(m)]


movings = {1: (0, -1), 2: (-1, -1), 3: (-1, 0), 4: (-1, 1), 5: (0, 1), 6: (1, 1), 7: (1, 0), 8: (1, -1)}

clouds = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]

for i in range(m):
    d = ds[i][0]
    s = ds[i][1]

    moved_clouds = []

    for x, y in clouds:
        cx = (x + (movings[d][0]) * s) % n
        cy = (y + (movings[d][1]) * s) % n
        
        moved_clouds.append((cx, cy))
        board[cx][cy] += 1

    for x, y in moved_clouds:
        for k in range(2, 9, 2):

            cx = x + movings[k][0]
            cy = y + movings[k][1]
            
            if cx < 0 or cx > n - 1 or cy < 0 or cy > n - 1:
                continue
            elif board[cx][cy] > 0:
                board[x][y] += 1
                
    new_clouds = []
    
    for j in range(n):
        for k in range(n):
            if not((j, k) in moved_clouds) and board[j][k] >= 2:
                new_clouds.append((j, k))
                board[j][k] -= 2

    clouds = new_clouds

water = 0

for i in range(n):
    water += sum(board[i])

print(water)