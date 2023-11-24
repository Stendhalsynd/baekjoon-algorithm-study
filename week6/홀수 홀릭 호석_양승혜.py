N = input()
counts = []

# 홀수인지 검사하는 함수
def isodd(strnum: str):
    count = 0
    for n in strnum:
        if int(n) % 2 == 1:
            count += 1
    return count

# 숫자의 길이기 1일때까지 재귀를 이용해서 홀수의 개수를 counts에 append하는 함수
def rec(n: str, total: int):
    if len(n) == 1:
        counts.append(total)
        return
    elif len(n) == 2:
        newnum = int(n[0]) + int(n[1])
        rec(str(newnum), total + isodd(str(newnum)))
    else:
        for i in range(1, len(n)):
            for j in range(i + 1, len(n)):
                num1, num2, num3 = int(n[ : i]), int(n[i : j]), int(n[j : ])
                newnum = num1 + num2 + num3
                rec(str(newnum), total + isodd(str(newnum)))
# 함수실행
rec(N, isodd(N))

# counts 배열의 최솟값, 최댓값 도출
print(min(counts), max(counts))
