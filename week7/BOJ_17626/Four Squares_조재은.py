'''
combinations_with_replacement : 입력된 반복 가능한 객체에서 중복을 허용하여 지정된 길이의 모든 조합을 생성합니다.
                                이 함수는 주어진 반복 가능한 객체에서 원소를 선택하여 지정된 횟수만큼 반복하여 조합을 만들 수 있도록합니다.
'''

from math import sqrt
from itertools import combinations_with_replacement

n = int(input())

square_1 = [i * i for i in range(1, int(sqrt(n)) + 1)]
square_2 = [sum(k) for k in combinations_with_replacement(square_1, 2)]

print(square_1)
print(square_2)

def answer(n):
    if n in square_1: #제곱수면
        return 1
    elif n in square_2: # 제곱수 두개를 더해서 만들 수 있는 수면
        return 2
    else:
        for square in square_1: # 제곱 수 중
            if n - square in square_2: # n에서 제곱수를 뺀 수가 제곱수 두개를 더해서 만들 수 있는 수면
                return 3
    return 4

print(answer(n))