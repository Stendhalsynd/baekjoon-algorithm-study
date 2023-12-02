import copy

def rotate(count, play, original):
    newMap = [[" "] * count for _ in range(count)]
    
    for i in range(count):
        for j in range(count):
            newMap[i][j] = original[i][j]

    for _ in range(play):

        for i in range(count):
            newMap[i][i] = original[count // 2][i]
            newMap[i][count // 2] = original[i][i]
            newMap[i][count - 1 - i] = original[i][count // 2]
            newMap[count // 2][i] = original[count - 1 - i][i]

        original = copy.deepcopy(newMap)

    return newMap

for _ in range(int(input())):
    n, angle = map(int, input().split())
    
    if angle >= 0:
        execute = angle // 45
    else:
        execute = (angle // 45 + 8) % 8

    numMap = []
    for _ in range(n):
        numMap.append(input().split())
    
    answerMap = rotate(n, execute, numMap)

    for num in answerMap:
        print(" ".join(num))
