import sys
from itertools import permutations

input = sys.stdin.readline

graph = []

for _ in range(3):
    graph.append(list(map(int, input().split())))

def check(values):
    global result

    new_square = []

    new_square.append(list(values[0:3]))
    new_square.append(list(values[3:6]))
    new_square.append(list(values[6:9]))

    if is_square(new_square):
        temp = 0

        for i in range(3):
            for j in range(3):
                temp += abs(graph[i][j] - new_square[i][j])

        result = min(result, temp)

def is_square(square):
    col_sum1 = sum(square[0])
    col_sum2 = sum(square[1])
    col_sum3 = sum(square[2])

    row_sum1 = square[0][0] + square[1][0] + square[2][0]
    row_sum2 = square[0][1] + square[1][1] + square[2][1]
    row_sum3 = square[0][2] + square[1][2] + square[2][2]

    di_sum1 = square[0][0] + square[1][1] + square[2][2]
    di_sum2 = square[0][2] + square[1][1] + square[2][0]

    if col_sum1 == col_sum2 == col_sum3 == row_sum1 == row_sum2 == row_sum3 == di_sum1 == di_sum2 == 15:
        return True
    else:
        return False

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = sys.maxsize

for i in permutations(numbers, 9):
    check(i)

print(result)
