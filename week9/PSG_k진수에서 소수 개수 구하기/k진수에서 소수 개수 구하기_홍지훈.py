from collections import deque
import math
def solution(n, k):
    # n : 양의 정수, k : 변환할 진수
    answer = 0
    
    # 1) k 진수로 일단 숫자를 바꿔보자
    def convert(n, k):
        curr = n
        que = deque([])
        while curr // k > 0:
            que.appendleft(curr % k)
            curr = curr // k
        if curr != 0:
            que.appendleft(curr % k)
        
        que = map(str, list(que))
        
        result = (''.join(que)).split('0')
        result = [x for x in result if x]
        return result
    
    def is_prime_number(num):
        if num == 1:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    
    stack = list(map(int, convert(n, k)))
    
    # 2) 소수 여부 판단
    for num in stack:
        if is_prime_number(num):
            answer += 1
    
    return answer

# 2번 풀이

# import math
# def solution(n, k):
#     # n : 양의 정수, k : 변환할 진수
#     answer = 0
    
#     # 1) k 진수로 일단 숫자를 바꿔보자
#     def convert(n, k):
#         result = ''
        
#         while n > 0:
#             n, rest = divmod(n, k)
#             result = str(rest) + result
        
#         return result
    
#     def is_prime_number(num):
#         if num == 1:
#             return False
#         for i in range(2, int(math.sqrt(num)) + 1):
#             if num % i == 0:
#                 return False
#         return True
    
#     stack = convert(n, k).split('0')
#     stack = [x for x in stack if x]
    
#     # 2) 소수 여부 판단
#     for num in stack:
#         if is_prime_number(int(num)):
#             answer += 1
    
#     return answer