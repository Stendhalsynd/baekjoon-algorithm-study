import sys

money = int(input())
stocks = list(map(int, input().split()))

# 준현
def jun():
    left_money = money
    stock_n = 0

    for stock in stocks:
        stock_n += left_money // stock
        left_money = left_money % stock
        if left_money == 0:
            break

    return left_money, stock_n

# 성민
def sung():
    left_money = money
    stock_n = 0
    for i in range(len(stocks)-4):
        if stocks[i] < stocks[i+1] < stocks[i+2] < stocks[i+3]:
            left_money += stock_n * stocks[i+3]
            stock_n = 0

        if stocks[i] > stocks[i + 1] > stocks[i + 2] > stocks[i + 3]:
            stock_n += left_money // stocks[i+3]
            left_money = left_money % stocks[i+3]

    return left_money, stock_n

jun_money, jun_stock = jun()
total_jun_money = jun_money + jun_stock * stocks[-1]
sung_money, sung_stock = sung()
total_sung_money = sung_money + sung_stock * stocks[-1]

if total_jun_money > total_sung_money:
    print("BNP")
elif total_jun_money < total_sung_money:
    print("TIMING")
else:
    print("SAMESAME")