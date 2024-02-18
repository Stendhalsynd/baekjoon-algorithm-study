import sys

input = sys.stdin.readline

N = int(input().strip())
length = list(map(int, input().split()))
price = list(map(int, input().split()))

result = 0
cur_money = price[0]

for i in range(N - 1):
    if price[i] < cur_money:
        cur_money = price[i]

    result += cur_money * length[i]

print(result)
