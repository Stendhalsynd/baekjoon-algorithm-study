n, m = map(int, input().split())
input = [list(input()) for _ in range(n)]   # 입력 값을 2중 리스트로 받음
answer = ""
total = 0

# DNA를 이루고 있는 4개의 염기 A, C, G, T : 사전순으로 비치함
for i in range(m):
    a, c, g, t = 0, 0, 0, 0
    for j in range(n):
        if input[j][i] == "A":
            a += 1
        elif input[j][i] == "C":
            c += 1
        elif input[j][i] == "G":
            g += 1
        else:
            t += 1
    if max(a, c, g, t) == a:
        answer += "A"
        total += c + g + t  # 가장 큰 염기의 수를 제외한 나머지 세 염기의 등장 횟수의 합이 hamming distance가 된다
    elif max(a, c, g, t) == c:
        answer += "C"
        total += a + g + t
    elif max(a, c, g, t) == g:
        answer += "G"
        total += a + c + t
    elif max(a, c, g, t) == t:
        answer += "T"
        total += a + c + g
print(answer)
print(total)
