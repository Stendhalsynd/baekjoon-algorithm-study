for _ in range(int(input())):
    n = int(input())
    # [['50', '10', '100', '20', '40'], ['30', '50', '70', '10', '60']]
    numList = [list(map(int, input().split())) for _ in range(2)]
    
    if n == 1:
        print(max(numList[0][-1], numList[1][-1]))
    
    else:
        numList[0][1] += numList[1][0]
        numList[1][1] += numList[0][0]
        for i in range(2, n):
            numList[0][i] += max(numList[1][i - 1], numList[1][i - 2])
            numList[1][i] += max(numList[0][i - 1], numList[0][i - 2])
        print(max(numList[0][-1], numList[1][-1]))
