from math import sqrt, floor
from itertools import combinations

n = int(input())

sqrt_list = list(range(1, floor(sqrt(n))+1))

break_point = False

for i in range(1, 5):
    for value in list(combinations(sqrt_list, i)):
        sum = 0
        for value2 in value:
            sum += value2 ** 2
            if sum == n:
                print(i)
                break_point = True
                break
        if break_point == True: break
    if break_point == True: break