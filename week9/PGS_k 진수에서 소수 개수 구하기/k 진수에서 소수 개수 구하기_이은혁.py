def solution(n, k):
    def change_to_k(num, k): # k진수로 변환
        result = ""
        while num > 0:
            result = str(num % k) + result
            num //= k
        return result

    def is_prime(num):
        if num<=1: return False
        if num==2: return True
        for i in range(2, int(num**0.5+1)):
            if num%i==0: return False
        return True

    ntok = change_to_k(n, k).split("0")
    ntok = list(map(int, filter(None, ntok)))
    answer = 0
    for num in ntok:
        if is_prime(num): answer+=1

    return answer

