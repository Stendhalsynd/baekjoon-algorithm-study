def drawStar(idx, number):
    if number == 1:
        starMap[idx][idx] = "*"
        return
    
    lens = 4 * number - 3
    for i in range(idx, lens + idx):
        # 위 아래
        starMap[idx][i] = "*"
        starMap[lens + idx - 1][i] = "*"

        # 양 옆
        starMap[i][idx] = "*"
        starMap[i][lens + idx - 1] = "*"
    
    return drawStar(idx + 2, number - 1)

n = int(input())
maxLen = 4 * n - 3
starMap = [[" "] * maxLen for _ in range(maxLen)]
drawStar(0, n)

for star in starMap:
    print("".join(star))
