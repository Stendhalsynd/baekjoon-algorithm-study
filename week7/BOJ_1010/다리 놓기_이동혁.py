from math import factorial

def combinations_count(n, r): # nCr의 조합의 개수를 구하는 함수
    return factorial(n) // (factorial(r) * factorial(n-r))

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    print(combinations_count(m, n))