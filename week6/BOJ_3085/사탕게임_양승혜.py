n = int(input())
candy = [list(input()) for _ in range(n)]
answer = 0

def check():
    maxNum = 1
    for i in range(n):
        temp = 1
        for j in range(1, n):
            if candy[i][j] == candy[i][j - 1]:
                temp += 1
            else:
                temp = 1
            maxNum = max(temp, maxNum)

        temp = 1
        for j in range(1, n):
            if candy[j][i] == candy[j - 1][i]:
                temp += 1
            else:
                temp = 1
            maxNum = max(temp, maxNum)
    return maxNum

for i in range(n):
    for j in range(n):
        if j + 1 < n and candy[i][j] != candy[i][j + 1]:
            # change column
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]
            answer = max(answer, check())
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]
            
        if i + 1 < n and candy[i][j] != candy[i + 1][j]:
            candy[i][j], candy[i + 1][j] = candy[i + 1][j], candy[i][j]
            answer = max(answer, check())
            candy[i][j], candy[i + 1][j] = candy[i + 1][j], candy[i][j]
            
print(answer)
