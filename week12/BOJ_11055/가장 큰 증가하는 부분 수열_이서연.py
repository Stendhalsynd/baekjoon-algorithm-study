# 첫 번째 풀이(오답) : target 값보다 작으면 모두 더하는 방식(증가하는 수열이라는 조건 미반영 - ex. 10 90 20 80 100 -> target이 100이면, 10+90+20+80+100=300이 결과로 나옴)
# import sys
# input = sys.stdin.readline

# num = int(input())

# list = list(map(int, input().split()))

# d = [0] * (num)

# sum = 0

# for i in range (0, num):
#     d[i] = list[i]
    
#     for j in range(0, i):
#         if list[j] < list[i]:
#             d[i] += list[j]
    
#     sum = max(sum, d[i])

# print(sum)

# 정답
import sys
import copy

input = sys.stdin.readline

num = int(input())

list = list(map(int, input().split()))

d = copy.deepcopy(list)


for i in range (0, num):
    for j in range (0, i):
        if list[j] < list[i]:
            d[i] = max(d[i], d[j] + list[i])
    
print(max(d))