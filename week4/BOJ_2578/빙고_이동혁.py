bingo_board = [list(map(int, input().split())) for _ in range(5)]
input_board = [list(map(int, input().split())) for _ in range(5)]
input_board = sum(input_board, [])

bool_board = [[0 for _ in range(5)] for _ in range(5)]

def find_index(value, matrix):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == value:
                return i, j

def find_bingo():
    total = 0
    for row in bool_board:
        if sum(row) == 5:
            total += 1

    for i in range(5):
        sum_temp = 0
        for j in range(5):
            sum_temp += bool_board[j][i]
        if sum_temp == 5:
            total += 1
    
    if bool_board[0][0] + bool_board[1][1] + bool_board[2][2] + bool_board[3][3] + bool_board[4][4] == 5:
        total += 1
    
    if bool_board[4][0] + bool_board[3][1] + bool_board[2][2] + bool_board[1][3] + bool_board[0][4] == 5:
        total += 1

    return total
            
for value in input_board:
    i, j = find_index(value, bingo_board)
    bool_board[i][j] = 1
    bingo = find_bingo()
    if bingo > 2:
        print(input_board.index(value) + 1)
        break