# 구현, 시뮬레이션
from itertools import chain

user = list(chain.from_iterable([list(map(int, input().split())) for _ in range(5)]))
nums = list(chain.from_iterable([list(map(int, input().split())) for _ in range(5)]))

rowDict = {0: 0, 1:0, 2:0, 3:0, 4:0}
colDict = {0: 0, 1:0, 2:0, 3:0, 4:0}

def bingo():
  diagonal1 = 0
  diagonal2 = 0
  for idx, val in enumerate(nums):
    index = user.index(val)
    row = index // 5
    col = index % 5
    rowDict[row] += 1
    colDict[col] += 1
    if row == col:
      diagonal1 += 1
    if (row + col) == 4:
      diagonal2 += 1

    if list(rowDict.values()).count(5) + list(colDict.values()).count(5) + diagonal1 // 5 + diagonal2 // 5 >= 3:
      print(idx + 1)
      return
    
bingo()