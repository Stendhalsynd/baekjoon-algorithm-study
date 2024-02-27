column, block = map(int, input().split())
height = list(map(int, input().split()))

answer = 0

if block == 1:
    # every cases
    answer += column
    # 0000
    for i in range(column - 3):
        if height[i] == height[i + 1] == height[i + 2] == height[i + 3]:
            answer += 1

if block == 2:
    # 00
    for i in range(column - 1):
        if height[i] == height[i + 1]:
            answer += 1

if block == 3:
    #001
    for i in range(column - 2):
        if height[i] == height[i + 1] == height[i + 2] - 1:
            answer += 1
    # 10
    for i in range(column - 1):
        if height[i] == height[i + 1] + 1:
            answer += 1

if block == 4:
    # 100
    for i in range(column - 2):
        if height[i] - 1 == height[i + 1] == height[i + 2]:
            answer += 1
    # 01
    for i in range(column - 1):
        if height[i] == height[i + 1] - 1:
            answer += 1

if block == 5:
    # 000, 101
    for i in range(column - 2):
        if height[i] == height[i + 1] == height[i + 2]:
            answer += 1
        if height[i] == height[i + 1] + 1 == height[i + 2]:
            answer += 1
    # 01, 10
    for i in range(column - 1):
        if height[i] == height[i + 1] - 1:
            answer += 1
        if height[i] == height[i + 1] + 1:
            answer += 1

if block == 6:
    # 000, 011
    for i in range(column - 2):
        if height[i] == height[i + 1] == height[i + 2]:
            answer += 1
        if height[i] + 1 == height[i + 1] == height[i + 2]:
            answer += 1
    # 00, 20
    for i in range(column - 1):
        if height[i] == height[i + 1]:
            answer += 1
        if height[i] == height[i + 1] + 2:
            answer += 1

if block == 7:
    # 000, 110
    for i in range(column - 2):
        if height[i] == height[i + 1] == height[i + 2]:
            answer += 1
        if height[i] == height[i + 1] == height[i + 2] + 1:
            answer += 1
    # 02, 00
    for i in range(column - 1):
        if height[i] + 2 == height[i + 1]:
            answer += 1
        if height[i] == height[i + 1]:
            answer += 1
            
print(answer)
