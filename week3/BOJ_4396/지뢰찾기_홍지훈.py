import sys

def findmine(n, graph1, graph2):
    def is_valid(row, col):
        return 0 <= row < n and 0 <= col < n

    def count_adjacent_mines(row, col):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        count = 0
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if is_valid(r, c) and graph1[r][c] == '*':
                count += 1
        return count

    for row in range(n):
        for col in range(n):

            if graph1[row][col] == '.' and graph2[row][col] == 'x':
                answer[row][col] = count_adjacent_mines(row, col)
            
            if graph1[row][col] == '*' and graph2[row][col] == 'x':
                for i in range(n):
                    for j in range(n):
                        if graph1[i][j] == '*':
                            answer[i][j] = '*'

# 입력 받기
n = int(sys.stdin.readline().rstrip())
graph1 = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
graph2 = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
answer = [['.'] * n for _ in range(n)] # . 으로 이루어진 answer 생성

# 결과 출력
findmine(n, graph1, graph2)
for i in range(n):
    for j in range(n):
        print(answer[i][j], end='')
    print()
