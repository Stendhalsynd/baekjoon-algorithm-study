import sys

input = sys.stdin.readline

T = int(input())

tests = []

for i in range(T):
    tests.append(str(input().strip()))

directions = [(0, 1), (-1 , 0), (0, -1), (1, 0)]

def move(idx, x, y):
    x += directions[idx][0]
    y += directions[idx][1]
    
    return x, y

for i in tests:
    tx, ty, cur_dir = 0, 0, 0
    top, bottom, left, right = 0, 0, 0, 0
    
    for j in i:
        if j == 'F':
            tx, ty = move(cur_dir, tx, ty)
            
            if cur_dir == 0 or cur_dir == (-4):
                top = max(top, ty)
            elif cur_dir == 1 or cur_dir == (-3):
                left = min(left, tx)
            elif cur_dir == 2 or cur_dir == (-2):
                bottom = min(bottom, ty)
            elif cur_dir == 3 or cur_dir == (-1):
                right = max(right, tx)
        elif j == 'B':
            if cur_dir >= 0:
                tx, ty = move((cur_dir + 2) % 4, tx, ty)
            else :
                tx, ty = move(cur_dir + 2, tx, ty)
                
            if cur_dir == 0 or cur_dir == (-4):
                bottom = min(bottom, ty)
            elif cur_dir == 1 or cur_dir == (-3):
                right = max(right, tx)
            elif cur_dir == 2 or cur_dir == (-2):
                top = max(top, ty)
            elif cur_dir == 3 or cur_dir == (-1):
                left = min(left, tx)
        elif j == 'L':
            cur_dir += 1
        elif j == 'R':
            cur_dir -= 1
            
        if cur_dir >= 0:
            cur_dir %= 4
        else :
            cur_dir %= (-4)
        
    print((top - bottom) * (right - left))
