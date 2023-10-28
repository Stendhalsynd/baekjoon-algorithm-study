# 구현, 시뮬레이션
import sys
from collections import deque

money = int(sys.stdin.readline().rstrip())
stockPrices = deque(list(map(int, sys.stdin.readline().rstrip().split())))

def BNP(money, stockPrices):
  stockSum = 0
  for stock in stockPrices:
    if money >= stock:
      buy = money // stock
      stockSum += buy
      money -= buy * stock
  return money + stockSum * stockPrices[-1]

def TIMING(money, stockPrices):
  stockSum = 0
  upStrike = 0
  downStrike = 0
  start = stockPrices.popleft()
  for stock in stockPrices:
    if start == stock:
      continue
    if start > stock:
      downStrike += 1
      upStrike = 0
    if start < stock:
      upStrike += 1
      downStrike = 0
    start = stock

    if upStrike == 3:
      if stockSum == 0:
        continue
      money += stockSum * stock
      stockSum = 0
      upStrike = 0
    if downStrike >= 3:
      if money < stock:
        continue
      buy = money // stock
      stockSum += buy
      money -= buy * stock
  return money + stockSum * stockPrices[-1]

print( "BNP" if BNP(money, stockPrices) > TIMING(money, stockPrices) else "SAMESAME" if BNP(money, stockPrices) == TIMING(money, stockPrices) else "TIMING")
