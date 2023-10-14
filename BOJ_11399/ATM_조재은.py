import sys

# 입력값 받기
n = int(input())
peoples = list(map(int, input().split()))

# 숫자 정렬하기
peoples.sort()

result = 0

# for문 이용해서 총계구하기
for i in range (1, n+1):
    result = result + sum(peoples[0:i]) # 0~i 번째까지의 합계 result에 넣기

print(result)
