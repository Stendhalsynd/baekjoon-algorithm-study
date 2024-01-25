r, c, n = map(int, input().split())
original = [list(input()) for _ in range(r)]

def bomb(grid):
    result = [['O'] * c for _ in range(r)]
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'O':
                result[i][j] = '.'
                for a, b in neighbors:
                    if 0 <= i + a < r and 0 <= j + b < c:
                        result[i + a][j + b] = '.'
    return result


if n == 1:  # 처음 상태 그대로 출력
    for row in original:
        print("".join(row))
elif n % 2 == 0:  # 다 'O'으로 가득 차있음
    for _ in range(r):
        print("O" * c)
elif n % 4 == 3:  # 처음 상태에서 한 번 터짐
    explosion1 = bomb(original)
    for row in explosion1:
        print("".join(row))
elif n % 4 == 1:  # 처음 상태에서 한 번 터지고, 이 터진 상태에서 한 번 더 폭발이 일어난다
    explosion1 = bomb(original)
    explosion2 = bomb(explosion1)
    for row in explosion2:
        print("".join(row))