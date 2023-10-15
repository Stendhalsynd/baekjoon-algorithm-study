import sys

# 입력값 받기
word = list(map(str, sys.stdin.readline().rstrip("\n")))
res = []

# 이중for문 이용해서 세단어로 나누기
for i in range(1, len(word)-1):
    for j in range(i+1, len(word)):
        fir = word[:i]  # 첫번째 단어
        sec = word[i:j] # 두번째 단어
        thi = word[j:]  # 세번째 단어

        # 역순
        fir.reverse()
        sec.reverse()
        thi.reverse()

        # 조인한 문자열들을 리스트에 추가
        res.append("".join(fir + sec + thi))

# 리스트 정렬
res.sort()

# 정렬 했으니 가장 첫 번째에 있는 문자열 출력
print(res[0])
# min(문자열)도 가능 알파벳 순서 상 앞에 오는 문자열 반환